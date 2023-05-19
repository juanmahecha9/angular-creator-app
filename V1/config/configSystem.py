import platform
import sys


class Config:
    def __init__(self, pwd, systemPlatform) -> None:
        self.pwd = pwd
        self.systemPlatform = systemPlatform

def getConfig():
    return Config(sys.argv[0],platform.system())
    