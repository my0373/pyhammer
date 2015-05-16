__author__ = 'Matt York myork@redhat.com'

import sys
import json

try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(1)

class Sat6(object):
    """
    A representation of a satellite 6 server
    """

    def __init__(self,
                 hostname,
                 username,
                 password,
                 https=False):

        # Get the connection settings
        self.hostname = hostname
        self.https = https
        self.post_headers = {'content-type': 'application/json'}
        self.put_headers = {'content-type': 'application/json'}

        if self.https:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

        self.username = username
        self.password = password

    def getOrganizationByName(self,organization_label):
        """
        Search for an organization by name, however we will only ever return the
        first result. This is easily changed by removing the [0] from the end of
        the line below.

        :param organization_label:
        :return:
        """
        return self.getRequest('katello/api/v2/organizations',
                               search=organization_label,
                               full_results='yes')['results'][0]

    def getOrganizationIDByName(self,organization_label):
        """
        This is a wrapper method to return just the id from the
        method getOrganizationByName.


        :param organization_label:
        :return:
        """
        return self.getOrganizationByName(organization_label)[u'id']

    def getContentViews(self,organization_id):
        """
        :param organization_id:
        :return:
        """
        return self.getRequest('katello/api/v2/content_views',
                               organization_id=organization_id)

    def moveHostCollectionHosts(self,org_id,old_host_collection,new_host_collection):
        """
        Method to move hosts from one host collection to another.
        It assumes we will move ALL hosts in the host collection.
        :param old_host_collection:
        :param new_host_collection:
        :return:
        """
        content_hosts = self.getContentHostsFromHC(org_id,old_host_collection)

        system_ids = [content_hosts[key]['uuid'] for key, val in content_hosts.iteritems()]

        #TODO: Nasty hack, not proud of it, will come back and refactor it later.
        hc_id = [content_hosts[key]['hc_id'] for key, val in content_hosts.iteritems()][0]

        new_hc_id = self.getHostCollectionID(org_id,new_host_collection)['host_collection_id']

        print "Removing from old HC"
        self.removeContentHostsFromHC(hc_id,system_ids)

        print "Adding to new HC"
        self.addContentHostsToHC(new_hc_id,system_ids)

        #return content_hosts['']

    def removeContentHostsFromHC(self,hc_id,system_ids):
        """
        Remove the content hosts specified in the list "system_id" by their uuid
        from the host collection specified by hc_id
        :param hc_id: The host collection id
        :param system_ids: a list of uuids to remove
        :return:
        """

        url = "katello/api/v2/host_collections/%s/remove_systems" % hc_id

        data = {'id':hc_id,
                'system_ids': system_ids}

        return self.putRequest(url,data)

    def addContentHostsToHC(self,hc_id,system_ids):
        """
        Add the content hosts specified in the list "system_id" by their uuid
        to the host collection specified by hc_id
        :param hc_id: The host collection id
        :param system_ids: a list of uuids to add
        :return:
        """

        url = "katello/api/v2/host_collections/%s/add_systems" % hc_id

        data = {'id':hc_id,
                'system_ids': system_ids}

        return self.putRequest(url,data)

    def getHostCollectionID(self,org_id,host_collection):
        """
        Get the content hosts from the named host collection.
        :param HostCollection:
        :return:
        """


        # Get the id, and content host totals of the host collection
        # that matches the name passed to us.
        url = 'katello/api/v2/organizations/%s/host_collections' % (org_id)
        host_collection_info = self.getRequest(url,
                                            organization_id=org_id,
                                            name=host_collection,
                                            )['results'][0]

        returndict = {}

        returndict['host_collection_id'] = host_collection_info['id']
        returndict['host_collection_hostcount'] = host_collection_info['total_content_hosts']

        return returndict


    def getContentHostsFromHC(self,org_id,host_collection):
        """
        Get the content hosts from the named host collection.
        :param HostCollection:
        :return:
        """


        hc_info = self.getHostCollectionID(org_id, host_collection)

        host_collection_id = hc_info['host_collection_id']
        host_collection_hostcount = hc_info['host_collection_hostcount']



        # So now we have the id for the host collection, we get a dump of all the
        # data for that collection, looking for 'host_collection_hostcount' number of hosts.
        # When we find them, we collect the hostname, uuid, and a single hc.

        # Please only assign a host to a single content group, otherwise it will
        # probably break this code.

        # We return this data as a dictionary.


        url = 'katello/api/v2/host_collections/%s/systems' % (host_collection_id)
        content_hosts = self.getRequest(url,id=host_collection_id)['results']

        returndict = {}
        for host in range (0,host_collection_hostcount):

            hostname = content_hosts[host]['name']
            uuid = content_hosts[host]['uuid']
            hostcollection = content_hosts[host]['hostCollections'][0]['name']
            id = content_hosts[host]['id']

            # The data structure we return
            returndict[hostname] = {u'uuid': uuid,
                                    u'name': hostname,
                                    u'hc': hostcollection,
                                    u'system_id': id,
                                    u'hc_id': host_collection_id,
                                    }


        return returndict


    def putRequest(self,url,data):

        self.url = url
        self.data = data

        # Generate the URL
        self.fullurl = "%s://%s/%s" % (self.protocol, self.hostname, self.url)



        r = requests.put(self.fullurl,
                         auth=(self.username,
                               self.password),
                         verify=self.https,
                         data=json.dumps(self.data),
                         headers=self.put_headers)
        print json.dumps(self.data)
        print r.url
        print r.status_code
        print r.reason


        return r

    def getRequest(self,url,**kwargs):
        """

        :param kwargs: The parameters we wat to include with our GET request
        :param url: The URL we are going to "GET"

        :return:
        """
        self.url = url

        # Generate the URL
        self.fullurl = "%s://%s/%s" % (self.protocol, self.hostname, self.url)


        r = requests.get(self.fullurl,
                         auth=(self.username,
                               self.password),
                         verify=self.https,
                         params=kwargs)




        # Quick sanity check for some well known codes
        if r.status_code == 404:
           print "GET Request %s failed. Got 404 not found" % r.url

        elif r.status_code == 403:
           print "GET Request %s failed. Got 403 Forbidden" % r.url

        elif r.status_code == 401:
           print "GET Request %s failed. Got 401 Unathorized" % r.url

        else:
            print "Got success code %d for request %s" % (r.status_code,
                                                          r.url)
        return r.json()

    def createLocation(self,location_name):
        """
        Create a new location object using POST and json.
        :param location_name:
        :return:
        """

        self.new_location = { "location[name]":location_name,
                              "name":location_name,
                              "Title":location_name,
                            }

        self.postRequest(url='/api/v2/locations',
                         data=self.new_location)

    def postRequest(self,url,data):
        """

        :param kwargs: The parameters we wat to include with our POST request
        :param url: The URL we are going to "POST"

        :return:
        """

        self.url = url
        self.data = data

        # Generate the URL
        self.fullurl = "%s://%s/%s" % (self.protocol, self.hostname, self.url)

        r = requests.post(self.fullurl,
                         auth=(self.username,
                               self.password),
                         verify=self.https,
                         data=json.dumps(self.data),
                         headers=self.post_headers)

        print r.reason




def main():

    # Yes these passowrds are left here deliberatly!
    s = Sat6(hostname='192.168.0.11',
             username='myork',
             password='redhat',
             https=False)

    #print s.getContentViews(0)
    #print s.getOrganizationByName('Default')
    oid = s.getOrganizationIDByName('Default')
    #s.moveHostCollectionHosts(oid, 'HC1', 'HC2')
    s.moveHostCollectionHosts(oid, 'HC2', 'HC1')
    #print s.createLocation('test123')


if __name__ == '__main__':
    main()