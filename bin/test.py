
## Import the sat6 library
from pyhammer.api import Sat6
from pyhammer.exceptions import NoOrganisationFound
import sys

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

    # Attempt to get the organisation id from the satellite, if we can't find it, handle the exception gracefully.
    # and exit.
    try:
        print s.getOrganizationByName(org_name)
    except NoOrganisationFound:
        print "No organisation '%s' was found on the satellite '%s'" % (org_name,hostname)
        logger.info("No organisation '%s' was found on the satellite '%s'" % (org_name,hostname))
        sys.exit(1)

    #oid = s.getOrganizationIDByName('Default')
    #s.moveHostCollectionHosts(oid, 'HC1', 'HC2')
    #s.moveHostCollectionHosts(oid, 'HC2', 'HC1')
    #print s.createLocation('test123')

if __name__ == '__main__':
    main()
