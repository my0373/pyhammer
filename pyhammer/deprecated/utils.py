__author__ = 'matt'


import os
import ConfigParser
import logging

def getSettingsFromFile(settings_file='~/.pyhammer_credentials'):

    config = ConfigParser.ConfigParser()
    path = os.path.expanduser(settings_file)
    print path
    logging.info("Loading settings from %s" % path)

    config.read(path)

    settings = {}

    settings["username"] = config.get('athentication',
                                      'username')

    settings["password"] = config.get('athentication','password')

    settings["server"] = config.get('server',
                                    'server')

    settings["organization"] = config.get('defaults',
                                          'organization')

    settings["loglevel"] = config.get('defaults',
                                      'loglevel')

    return settings





if __name__ == '__main__':
    print 'test'
    print getSettingsFromFile()