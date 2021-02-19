from configparser import ConfigParser

def getKey(key):
    return getConfig('project.cfg', key)

def getConfig(cfgFile, key):
    config = ConfigParser()
    config.read(cfgFile)
    section = config.sections()[0]
    return config.get(section, key)