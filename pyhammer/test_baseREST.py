from unittest import TestCase

__author__ = 'myork'


class TestBaseREST(TestCase):
    def setUp(self):
        self.hostname = '192.168.100.3'
        self.username = 'admin'
        self.password = 'redhat'
        self.valid_org_name = 'Redhat_Consulting'
        self.invalid_org_name = 'Badge'


    def test_getRequest_valid_query(self):
        self.fail()

    def test_getRequest_invalid_query(self):
        self.fail()

    def test_getRequest_valid_server(self):
        self.fail()

    def test_getRequest_invalid_server(self):
        self.fail()



    def test_putRequest(self):
        self.fail()

    def test_postRequest(self):
        self.fail()

    def test_deleteRequest(self):
        self.fail()
