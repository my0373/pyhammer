from pyhammer.organizations import Organization
import logging



__author__ = 'myork'

loglevel = logging.CRITICAL
username = 'myork'
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
    print a.getOrganizationByLabel('redhat')




if __name__ == '__main__':
    logging.basicConfig(level=loglevel)
    logger = logging.getLogger(__name__)

    testOrgQuery()

