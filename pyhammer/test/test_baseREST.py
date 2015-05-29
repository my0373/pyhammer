from unittest import TestCase
import requests
from mock import Mock, patch
from pyhammer.baserestpy import BaseREST

__author__ = 'myork'


class TestBaseREST(TestCase):
    def setUp(self):
        self.hostname = '192.168.100.3'
        self.username = 'admin'
        self.password = 'redhat'
        self.valid_org_name = 'Redhat_Consulting'
        self.invalid_org_name = 'Badge'
        self.http = False

        # Create a test object
        self.br = BaseREST(hostname=self.hostname,
                      username=self.username,
                      password=self.password,
                      https=self.http)


    def tearDown(self):
        self.br = None



    def test_getRequest_valid_query(self):
        url = "katello/api/v2/organizations"
        data = {"search":self.valid_org_name,
                "full_results":"no"}

                # Dummy dictionary response from the Mock
        fakejsonresult = {u'sort':
                              {u'by': None, u'order': None},
                          u'search': u'Redhat_Consulting', u'results': [
                                                                        {u'description': u'Redhat_Consulting',
                                                                         u'title': u'Redhat_Consulting',
                                                                         u'created_at': u'2015-05-20T19:36:42Z',
                                                                         u'updated_at': u'2015-05-25T00:19:08Z',
                                                                         u'label': u'Redhat_Consulting',
                                                                         u'id': 5,
                                                                         u'name': u'Redhat_Consulting'}
                                                                       ], u'per_page': 20,
                          u'total': 2,
                          u'subtotal': 1,
                          u'page': 1
                          }

        with patch.object(requests,'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            #mock_response.json = fakejsonresult

            assert result == 200


