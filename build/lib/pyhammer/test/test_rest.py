from unittest import TestCase

# The requests module

from pyhammer.lib.exceptions import RESTAuthenticationFailure

import logging

# The mock module to allow proper unit testing
import mock

# The lowest level module that handles rest requests.
from pyhammer.lib.rest import BaseREST


class TestGetRequest(TestCase):
    @mock.patch('pyhammer.lib.rest.BaseREST.restRequest')
    def testBadPassword(self, mock_requests):
    #def testBadPassword(self):
        '''
        Simple test using mock for a get request.

        Here we mock the internal restRequest method so it always returns a fail to login message.
        '''

        url = "katello/api/v2/organizations"

        username = 'admin'
        password = 'redhat'
        https = False
        hostname = '192.168.100.3'
        organization_label = 'Redhat_Consulting'
        protocol = 'http'

        badresult = {'status_code': 401, u'error': {u'message': u'Unable to authenticate user admin'}}

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (protocol, hostname, url)

        # Spoof the return value
        mock_requests.return_value = badresult

        tc = BaseREST(hostname,username,password,https)
        data = {}

        with self.assertRaises(RESTAuthenticationFailure):
            tc.getRequest(url,data)

    @mock.patch('pyhammer.lib.rest.BaseREST.restRequest')
    def testGoodPassword(self, mock_requests):
        '''
        Simple test using mock for a get request.

        Here we mock the internal getRequest method with a successful login message.

        '''

        url = "katello/api/v2/organizations"
        loglevel = logging.CRITICAL
        username = 'admin'
        password = 'redhat'
        https = False
        hostname = '192.168.100.3'
        protocol = 'http'

        goodresult = {u'sort': {u'by': None, u'order': None}, u'search': None, 'status_code': 200, u'results': [{u'description': u'Redhat_Consulting', u'title': u'Redhat_Consulting', u'created_at': u'2015-06-15T13:01:34Z', u'updated_at': u'2015-06-15T13:04:32Z', u'label': u'Redhat_Consulting', u'id': 3, u'name': u'Redhat_Consulting'}], u'per_page': 20, u'total': 1, u'subtotal': 1, u'page': 1}
        badresult = {'status_code': 401, u'error': {u'message': u'Unable to authenticate user admin'}}

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (protocol, hostname, url)

        # Spoof the return value
        mock_requests.return_value = goodresult

        tc = BaseREST(hostname,username,password,https)
        data = {}

        self.assertEquals(tc.getRequest(url,data),goodresult)

