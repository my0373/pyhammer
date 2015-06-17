__author__ = 'myork'





from pyhammer.lib.exceptions import OrganizationNotFound
from pyhammer.lib.rest import BaseREST

class Organization(object):
    """
    A class to abstract organisation API calls to Satellite 6
    """
    def __init__(self,hostname,username,password,https=False):
        self.api = BaseREST(hostname,
                            username,
                            password,
                            https)

    def createOrganization(self,label,name=None,description=None):
        """
        Create an organization
        """

        # The URL to pass to the post request
        url = "katello/api/v2/organizations"

        # Define the data
        data = {'label':label,
                'name':name,
                'description':description}

        # Execute the create request
        return self.api.postRequest(url,data)

    def deleteOrganizationByID(self,org_id):
        """
        Delete an organisation by the Org ID
        """
        # The URL to pass to the GET request
        url = "katello/api/v2/organizations/%s/" % org_id

        data = {"id":org_id,}

        return self.api.deleteRequest(url,data)

    def deleteOrganizationByLabel(self,label):
        org_id = self.getOrganizationByLabel(label)['id']
        self.deleteOrganizationByID(org_id)

    def getAllOrganizationsIndexByID(self):
        """
        Get all organizations and use the organization ID as
        the key on the resulting dictionary.
        :return:
        """
        # The URL to pass to the GET request
        url = "katello/api/v2/organizations"

        # The structured JSON data we will pass
        data = {'full_results':True,
                'per_page':9999,
               }

        # Define the return dictionary
        orgdict = {}

        # Execute the get request to get all the organisations.
        # Strip the results and return a dict of organizations with the label as a key,
        # and a dict of organisation attributes as a value.
        for org in self.api.getRequest(url,data)['results']:
            orgdict[int(org["id"])] = org


        return orgdict

    def getAllOrganizationsIndexByLabel(self):
        """
        Get all organizations and use the label as the key on the resulting dictionary.
        :return:
        """
        # The URL to pass to the GET request
        url = "katello/api/v2/organizations"

        # The structured JSON data we will pass
        data = {'per_page':10,
                'page':1,
                'sort[order]':'ASC',
               }

        # Define the return dictionary
        orgdict = {}

        # Execute the get request to get all the organisations.
        # Strip the results and return a dict of organizations with the label as a key,
        # and a dict of organisation attributes as a value.
        for org in self.api.getRequest(url,data)['results']:
            orgdict[str(org["label"])] = org

        return orgdict

    def getAllOrganizations(self):
        """
        Query the satellite server for a list of organisations.
        :return:
        """
        return self.getAllOrganizationsIndexByLabel()

    def getOrganizationByLabel(self,label):
        """
        Query the satellite server for an organisation with a specific label.
        :return:
        """

        orgs = self.getAllOrganizationsIndexByLabel()

        try:
            result =  orgs[label]
        except KeyError:
            raise OrganizationNotFound()

        return result

    def getOrganizationByID(self,org_id):
        """
        Query the satellite server for an organisation with a specific organization ID.
        :return:
        """

        orgs = self.getAllOrganizationsIndexByID()

        try:
            result = orgs[org_id]
        except KeyError:
            raise OrganizationNotFound()

        return result







