
## Import the sat6 library
from pyhammer.api import Sat6
import logging

__author__ = 'myork'

loglevel = logging.INFO
username = 'myork'
password = 'redhat'
https = False
hostname = '192.168.100.3'

def main():


    logging.basicConfig(level=loglevel)
    logger = logging.getLogger(__name__)

    # Yes these passowrds are left here deliberatly!
    s = Sat6(hostname=hostname,
             username= username,
             password=password,
             https=https)

    logging.info("Username: %s" % username )


    org_name = 'Redhat_Consulting'

    #print s.getContentViews(0)
    print s.getOrganizationByName(org_name)
    #oid = s.getOrganizationIDByName('Default')
    #s.moveHostCollectionHosts(oid, 'HC1', 'HC2')
    #s.moveHostCollectionHosts(oid, 'HC2', 'HC1')
    #print s.createLocation('test123')

if __name__ == '__main__':
    main()
