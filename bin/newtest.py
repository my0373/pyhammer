import logging

from pyhammer.lib.organizations import Organization
from pyhammer.lib.credentials import Credentials

__author__ = 'myork'



loglevel = logging.CRITICAL


def testOrgQuery():
    credentials = Credentials()

    a = Organization(hostname=credentials.server,
                    username=credentials.username,
                    password=credentials.password,
                    https=credentials.https)

    #print a.getAllOrganizations()
    print a.getOrganizationByLabel(credentials.organization)




if __name__ == '__main__':
    logging.basicConfig(level=loglevel)
    logger = logging.getLogger(__name__)

    testOrgQuery()

