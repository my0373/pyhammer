
## Import the sat6 library
from pyhammer.api import Sat6

__author__ = 'myork'

def main():

    # Yes these passowrds are left here deliberatly!
    s = Sat6(hostname='192.168.100.3',
             username='myork',
             password='redhat',
             https=False)
    org_name = 'Redhat_Consultingss'

    #print s.getContentViews(0)
    print s.getOrganizationByName(org_name)
    #oid = s.getOrganizationIDByName('Default')
    #s.moveHostCollectionHosts(oid, 'HC1', 'HC2')
    #s.moveHostCollectionHosts(oid, 'HC2', 'HC1')
    #print s.createLocation('test123')

if __name__ == '__main__':
    main()
