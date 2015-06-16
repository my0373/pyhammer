import logging

from pyhammer.lib.organizations import Organization

__author__ = 'myork'

loglevel = logging.CRITICAL
username = 'admin'
password = 'redhat'
https = False
hostname = '192.168.100.3'
organization_label = 'Redhat_Consulting'


def testOrgQuery():
    a = Organization(hostname,
                    username,
                    password,
                    https)

    #print a.getAllOrganizations()
    print a.getOrganizationByLabel('Redhat_Consulting')




if __name__ == '__main__':
    logging.basicConfig(level=loglevel)
    logger = logging.getLogger(__name__)

    testOrgQuery()

