import json
import os
import shutil
import sys
import time

import pyfiglet

# Dependencias del programa
from config.configSystem import getConfig
from src.admin.Angular.angular import angular
from src.client.projectName import projectName
from src.interface.interface import gui

DATAPROJECT = gui()

pwd = getConfig().pwd.replace("/main.py", "")
systemPlatform = getConfig().systemPlatform


def projectCreator(pwd: str, use: str, files: str):
    # Variable para la copia de los archivos insumo del proyecto (fonts, images, icons, etc)
    pwdFiles = files
    # Crear carpeta para el poyecto
    if (use == "Y" or use == "y"):
        pwdFront = pwd + "/frontend"
        if not os.path.exists(pwdFront):
            os.makedirs(pwdFront)
        # Capturar el nombre del nuevo proyecto
        newProject = DATAPROJECT[1]
        time.sleep(1)
        # Inicializar el nuevo proyecto
        angular(pwdFront, newProject, systemPlatform, pwdFiles)
    else:
        # Capturar el nombre del nuevo proyecto
        newProject = DATAPROJECT[1]
        time.sleep(1)
        # Inicializar el nuevo proyecto
        angular(pwd, newProject, systemPlatform, pwdFiles)


if __name__ == "__main__":
    CRED = '\033[91m'
    CEND = '\033[0m'
    try:
        ascii_banner = pyfiglet.figlet_format(
            "Angular \n Projects \n Builder!")
        print(CRED + ascii_banner + CEND)
    except Exception as e:
        print("Angular Projects Builder")

    print(CRED + "Version: 2.4" + CEND)
    print("")
    print("")
    time.sleep(3)
    print("Platform system: " + systemPlatform)
    time.sleep(1)
    #print(CRED + f"\n The default PWD is:  {pwd} \n Do you will like use this path?  (Y) or Do you will like use a custom path? (n) " + CEND)
    selectionPwd = 'N'
    selectionPwd = selectionPwd.upper()

    # Seleccion de tipo de ruta a usar para crear el proyecto
    # Y usar la carpeta actual
    # N usar una carpeta custom
    # if selectionPwd == "Y":
    #print(f"\n You are located into {pwd} \n")
    # time.sleep(1)
    #projectCreator(pwd, "Y", pwd)
    # else:
    pathSelected = DATAPROJECT[0].replace("\\", "/")
    time.sleep(1)
    print("Your path is: ", pathSelected)
    projectCreator(pathSelected, "N", os.getcwd())
