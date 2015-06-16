__author__ = 'myork'

from pyhammer.lib.organizations import Organization

hostname = "192.168.100.3"
username = "admin"
password = "redhat"
https = False

og = Organization(hostname,username,password,https)
print og.getAllOrganizationsIndexByID()