import sys
import platform

class config:
    def __init__(self, pwd, platform_system) -> None:
        self.pwd = pwd
        self.platform_system = platform_system
        pass
    
def set_config():
    return config(sys.argv[0], platform.system())