__author__ = 'Matt York (myork@redhat.com)'
"""
This module holds only the primitive REST methods.
I've seperated them out for ease of testing, and for clarity.

"""

from logwrapper import *

import exceptions

import requests


import json

class BaseREST(object):
    """
    The Base REST library.

    It uses the 'requests' library for all communication
    this in turn uses urllib to dispatch.

    Each async "conversation" with the server should use a new instance of this module,
    the reason being that when this class is instansiated, a contextid is generated.

    We can use this context id to follow "conversations" which makes it easier to debug.
    """
    def __init__(self,hostname,username,password,https=False):

        """

        :return:
        """
        # When we create a new instance, we create a new internal contextid.
        # This is exposed as an attribute, which allows us to track "conversations".
        self.cid = id(self)

        # Create instance attributes for each parameter
        self.hostname = hostname
        self.username = username
        self.password = password
        self.https = https
        self.post_headers = {u'content-type': u'application/json'}
        self.put_headers = {'content-type': 'application/json'}
        self.delete_headers = {'content-type': 'application/json'}

        # settings debug if required.
        logdebug("Creating context",self.cid)
        logdebug("hostname = %s" % (self.hostname),self.cid)
        logdebug("username = %s" % (self.username),self.cid)
        logdebug("password = %s" % (self.password),self.cid)
        logdebug("https = %s" % (self.https),self.cid)
        logdebug("post_headers = %s" % (self.post_headers),self.cid)
        logdebug("put_headers = %s" % (self.put_headers),self.cid)
        logdebug("delete_headers = %s" % (self.delete_headers),self.cid)

        # Decide if we are going to use HTTP or HTTPS
        if self.https:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

        logdebug("protocol = %s" % (self.protocol),self.cid)


    def restRequest(self,rtype,url,data=None):
        """
        This is the only method that will actually make a call to the REST interface.
        """
        # Log the request type, url and the Context ID
        loginfo("%s Request %s" % (rtype.upper(), url), self.cid)

        # If the request is a GET request
        if rtype.lower() in 'get':
            restresponse = requests.get(url,
                                        auth=(self.username,
                                              self.password),
                                        verify=self.https,
                                        params=data)


        # If the request is a POST request                               )
        elif rtype.lower() in 'post':
            restresponse = requests.post(url,
                                        auth=(self.username,
                                              self.password),
                                        verify=self.https,
                                        data=json.dumps(data),
                                        headers=self.post_headers)

        # If the request is a DELETE request
        elif rtype.lower() in 'delete':
            restresponse = requests.delete(url,
                                        auth=(self.username,
                                              self.password),
                                        verify=self.https,
                                        params=data)
            pass

        # If the request is a PUT request
        elif rtype.lower() in 'put':
            restresponse = requests.put(url,
                                        auth=(self.username,
                                              self.password),
                                        verify=self.https,
                                        params=data)

        # Capture the HTTP status code, and json packed results
        return restresponse

    def getRequest(self, url, data):
        """
        Execute a GET request and return
        :return:
        """
        requesttype = 'GET'

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (self.protocol, self.hostname, url)

        # Issue the request
        requestResult = self.restRequest(requesttype,
                                fullurl,
                                json.dumps(data))


        # Collect the HTTP status code
        result_code = requestResult.status_code


        # Unpack the results from HTTP response
        json_results = requestResult.json()

        # Log the fact we have run
        loginfo("Request completed with status code %d" % (result_code), self.cid)
        loginfo("Request completed with json results %s" % (json_results), self.cid)



        # Return the unpacked results
        return json_results

    def postRequest(self, url, data):
        """
        Execute a POST request and return
        :return:
        """
        requesttype = 'POST'

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (self.protocol, self.hostname, url)

        # Issue the request
        return self.restRequest(requesttype,
                         fullurl,
                         data)

    def putRequest(self, url, data):
        """
        Execute a PUT request and return
        :return:
        """
        requesttype = 'PUT'

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (self.protocol, self.hostname, url)

        # Issue the request
        return self.restRequest(requesttype,
                         fullurl,
                         data)

    def deleteRequest(self, url, data):
        """
        Execute a DELETE request and return
        :return:
        """
        requesttype = 'DELETE'

        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (self.protocol, self.hostname, url)

        # Issue the request
        return self.restRequest(requesttype,
                         fullurl,
                         data)
