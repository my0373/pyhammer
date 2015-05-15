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

    def getContentViews(self,organization_id):
        """
        :param organization_id:
        :return:
        """
        return self.getRequest('katello/api/v2/content_views',
                               organization_id=organization_id)

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


def main():

    s = Sat6(hostname='satellite3.maclab',
             username='myork',
             password='redhat',
             https=False)

    print s.getContentViews(0)
    print s.getOrganizationByName('Default')


if __name__ == '__main__':
    main()