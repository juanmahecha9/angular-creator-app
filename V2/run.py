# /bin/bash

import os
import sys
import time
import json
import shutil
import pyfiglet

from config.config import set_config
from project.interface.interface import gui
from project.angular.creation import creation_project
from project.src.cli.init_node import creartion_project_node

# Constantes del sistema
(NEWPWD, PROJECTNAME, STYLE, BACKEND) = gui()

FILE = __file__.replace('\\', '/').split('/')[-1]
PWD = set_config().pwd.replace(FILE, '')
PLATFORM = set_config().platform_system
 # Verificar si el PATH termina con /
tmp_path = NEWPWD.replace('\\', '/')
if (tmp_path.endswith('/')):
    tmp_path = tmp_path[:-1]
tmp_project_name = PROJECTNAME.lower()
theme = STYLE

def frontend():
    try:
        print('Fronted')
        ascii_banner = pyfiglet.figlet_format(
            "Angular \n Projects \n Builder!")
        print(ascii_banner)
        print("Version: 2.4")
        print("_____________")
        print("_____________")
        print("Your system:", PLATFORM)
        print("_____________")
        creation_project(f'{tmp_path}/{tmp_project_name}',
                         tmp_project_name, theme)
    except Exception as err:
        print("Error:", err)

def backend():
    try:
        print('Backend')
        ascii_banner = pyfiglet.figlet_format(
            "API REST \n Projects \n Builder!")
        print(ascii_banner)
        print("Version: 2.4")
        print("Node.js: TypeScript")
        print("_____________")
        print("_____________")
        print("Your system:", PLATFORM)
        print("_____________")
        creartion_project_node(f'{tmp_path}/{tmp_project_name}')
    except Exception as err:
        print("Error:", err)
        
if __name__ == '__main__':
    os.system(f'cd {tmp_path} && mkdir {tmp_project_name}')
    # inicializar el aplicativo
    if(BACKEND == 'si'):
        print('Creacion Front service y Back service')
        backend()
        print('Finalizando construccion aplicativo rest')
        time.sleep(5)
        frontend()
        print('Finalizando construccion aplicativo front')
    else:
        print('Creacion Front service')
        frontend()
        print('Finalizando construccion aplicativo front')
        
        
    
    
    
    
    
    
   