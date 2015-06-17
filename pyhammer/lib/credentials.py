__author__ = 'myork'

import ConfigParser
import os

class Credentials():
    def __init__(self,configfile=None):
        """
        We expect to find a files called ~.pyhammer

        With content similar to the following

        [satellite]
        username=admin
        password=redhat
        server=192.168.100.3
        protocol=http

        [organization]
        default_organization=Redhat_Consulting

        """

        # Make sure we have a valid config file, and that it exists.
        if configfile:
            self.configfile = configfile
        else:
            self.configfile = os.path.expanduser('~/.pyhammer')
            if not os.path.isfile(self.configfile):
                self.configfile = None

        if self.configfile:
            self.config = ConfigParser.SafeConfigParser()
            self.config.read(self.configfile)

            # Assign values from the config file to instance attributes
            self.username = self.config.get('satellite','username')
            self.password = self.config.get('satellite','password')
            self.server = self.config.get('satellite','server')
            self.protocol = self.config.get('satellite','protocol')
            self.organization = self.config.get('organization','default_organization')
            if self.protocol == "https":
                self.https = True
            else:
                self.https = False






if __name__ == '__main__':
    c = Credentials()
    print c.username
    print c.password
    print c.server
    print c.protocol
    print c.organization
    print c.https








