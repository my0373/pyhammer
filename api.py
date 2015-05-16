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
        return self.getRequest('/katello/api/v2/organizations',
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
        return content_hosts

    def removeContentHostsFromHC(self,):
        "/katello/api/v2/host_collections/:id/remove_systems"

    def getContentHostsFromHC(self,org_id,host_collection):
        """
        Get the content hosts from the named host collection.
        :param HostCollection:
        :return:
        """


        # Get the id, and content host totals of the host collection
        # that matches the name passed to us.
        url = '/katello/api/v2/organizations/%s/host_collections' % (org_id)
        host_collection_info = self.getRequest(url,
                                            organization_id=org_id,
                                            name=host_collection,
                                            )['results'][0]

        host_collection_id = host_collection_info['id']
        host_collection_hostcount = host_collection_info['total_content_hosts']



        # So now we have the id for the host collection, we get a dump of all the
        # data for that collection, looking for 'host_collection_hostcount' number of hosts.
        # When we find them, we collect the hostname, uuid, and a single hc.

        # Please only assign a host to a single content group, otherwise it will
        # probably break this code.

        # We return this data as a dictionary.


        url = '/katello/api/v2/host_collections/%s/systems' % (host_collection_id)
        content_hosts = self.getRequest(url,id=host_collection_id)['results']

        returndict = {}
        for host in range (0,host_collection_hostcount):

            hostname = content_hosts[host]['name']
            uuid = content_hosts[host]['uuid']
            hostcollection = content_hosts[host]['hostCollections'][0]['name']

            returndict[hostname] = {u'uuid': uuid,
                                    u'name': hostname,
                                    u'hc': hostcollection,
                                    }

        return returndict

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
    s.moveHostCollectionHosts(oid, 'HC1', 'HC2')
    #print s.createLocation('test123')


if __name__ == '__main__':
    main()