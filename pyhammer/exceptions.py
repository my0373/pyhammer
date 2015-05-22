__author__ = 'myork'
import logging

class OrganizationNotFound(Exception):
    pass

class FailToDeleteOrganization(Exception):
    def __init__(self,status_code,
                 message,
                 organization_id):
        self.code = status_code
        self.message = message
        self.org_id = organization_id
        self.errmsg = 'Unable to delete organization id %d because %s' % (self.org_id,
                                                                          self.message)
        logging.error(self.errmsg)


class FailToCreateOrganization(Exception):

    def __init__(self,status_code,message,organization_name):

        self.code = status_code
        self.msg = message
        self.org_name = organization_name
        self.errmsg = "Unable to create organization %s because %s" % (self.org_name,
                                                                      self.msg)
        logging.error(self.errmsg)

