__author__ = 'Matt York (myork@redhat.com)'
"""
This module holds only the primitave REST methods.
I've seperated them out for ease of testing, and for clarity.


"""

from random import Random
import logging
from logwrapper import *
import requests

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
        logdebug("Creating context",self.cid)

        # Create instance attributes for each parameter
        self.hostname = hostname
        logdebug("hostname = %s" % (self.hostname),self.cid)
        self.username = username
        logdebug("username = %s" % (self.username),self.cid)
        self.password = password
        logdebug("password = %s" % (self.password),self.cid)
        self.https = https
        logdebug("https = %s" % (self.https),self.cid)

        # Decide if we are going to use HTTP or HTTPS
        if self.https:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

        logdebug("protocol = %s" % (self.protocol),self.cid)


    def getRequest(self, url, data):
        """
        Execute a GET request.
        :return:
        """


        # Generate a complete url from the request path.
        fullurl = "%s://%s/%s" % (self.protocol, self.hostname, url)

        # Let the user know we are making a GET request.
        loginfo("GET Request %s" %(fullurl),self.cid)



        # Log a nice info message to be clear.
        loginfo("URL=%s" %(fullurl),self.cid)

        # Now we actually issue the GET request to the server
        restresponse = requests.get(fullurl,
                                    auth=(self.username,
                                          self.password),
                                    verify=self.https,
                                    params=data)
        return restresponse



    def putRequest(self):
        """
        Execute a PUT request.
        :return:
        """
        pass

    def postRequest(self):
        """
        Execute a POST request.
        :return:
        """

        pass

    def deleteRequest(self):
        """
        Execute a DELETE request.
        :return:
        """
        pass


