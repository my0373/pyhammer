__author__ = 'myork'

from pyhammer.lib.organizations import Organization
from pyhammer.lib.credentials import Credentials

creds = Credentials()
hostname = creds.server
username = creds.username
password = creds.password
https = creds.https

org = Organization(hostname,username,password,https)

# Create bulk organizations
#for i in range(1,40):
#    org_label = str(i)
#    print org.createOrganization(org_label,org_label,org_label)

#print org.createOrganization('timmy2','timmy2','timmytime')
#org.deleteOrganizationByID(5)
#print org.getAllOrganizationsIndexByID()
#org.deleteOrganizationByLabel("timmy")
print org.getAllOrganizations().keys()