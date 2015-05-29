from unittest import TestCase
import logging

from pyhammer.deprecated.api import Sat6
from pyhammer.exceptions import *

__author__ = 'myork'

class TestRESTPrimitives(TestCase):
    def setUp(self):
        """
        Initial test setup
        """
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logging.debug("Starting setup")
        self.hostname = '192.168.100.3'
        self.username = 'admin'
        self.password = 'redhat'
        self.https = False
        self.testorgname = "Test Organization"
        self.testorglabel = "Test_Organization"
        self.testorgdescription = "Test Description Of \n this Organization"

        self.sat6 = Sat6(hostname=self.hostname,
                         username=self.username,
                         password=self.password,
                         https=False)


        logging.debug("Finishing setup")


class TestOrganizations(TestCase):
    def setUp(self):
        """
        Initial test setup
        """
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logging.debug("Starting setup")
        self.hostname = '192.168.100.3'
        self.username = 'admin'
        self.password = 'redhat'
        self.https = False
        self.testorgname = "Test Organization"
        self.testorglabel = "Test_Organization"
        self.testorgdescription = "Test Description Of \n this Organization"

        self.sat6 = Sat6(hostname=self.hostname,
                         username=self.username,
                         password=self.password,
                         https=False)


        logging.debug("Finishing setup")

    def tearDown(self):
        """
        Delete any test organizations we have created.
        """
        logging.debug("Staring Teardown")
        try:
            org_id = self.sat6.getOrganizationIDByName(self.testorgname)
            self.sat6.deleteOrganization(org_id,99)
        except OrganizationNotFound:
            pass

        logging.debug("Finished Teardown")


    def test_createOrganization(self):
        """
        Test we can create a new organization
        """

        # Delete the test organization if it already exists.
        # Ignore any errors.
        try:
            org_id = self.sat6.getOrganizationIDByName(self.testorgname)
            self.sat6.deleteOrganization(org_id,3)
        except OrganizationNotFound:
            pass


        # Create a new organization
        result = self.sat6.createOrganization(name=self.testorgname,
                                     label=self.testorglabel,
                                     description=self.testorgdescription,
                                    )

        self.assertTrue(result)

    def test_deleteOrganization(self):
        """
        Test we can delete an organization.
        """

        # Attempt to create a test organisation if it does't already exist.
        try:
            self.sat6.createOrganization(name=self.testorgname,
                                         label=self.testorglabel,
                                         description=self.testorgdescription,
                                         )

        except FailToCreateOrganization:
            pass

        # Get the details of the organisation, and delete it.
        org_id = self.sat6.getOrganizationIDByName(self.testorgname)
        result = self.sat6.deleteOrganization(org_id,1)

        
        self.assertTrue(result)


