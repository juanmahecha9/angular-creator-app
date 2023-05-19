import os
import time

folders = ['components', 'models', 'guards', 'services', 'modules', 'common']

scriptFolderUnix = {
    "components": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g c  "project/components/$1"  --module app 
    shift 
done
    """,
    "models": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g class  "util/models/$1"  
    shift 
done
    """,
    "guards": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g guard  "util/guards/$1"  
    shift 
done
    """,
    "services": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g s  "util/services/$1"  
    shift 
done
    """,
    "modules": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g m  "project/modules/$1" --module app --route $1 
    shift 
done
    """,
    "common": """#!/bin/bash 
while [ "$1" != "" ]; do 
    npx ng g c  "project/common/components/$1" --module app 
    shift 
done
    """,
}
scriptFolderWindows = {
    "components": """@echo off
set component=c
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% project/components/%%a 
)
    """,
    "models": """@echo off
set component=class
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% util/models/%%a 
)
    """,
    "guards": """@echo off
set component=guard
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% util/guards/%%a 
)
    """,
    "services": """@echo off
set component=s
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% util/services/%%a
)
    """,
    "modules": """@echo off
set component=m
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% project/modules/%%a --module app --route %%a
)
    """,
    "common": """@echo off
set component=c
::Create Multiple %component% with batch file
set "list=%*"
for %%a in (%list%) do (
    npx ng g %component% project/common/components/%%a 
)
    """,
}


def scripts(pwd: any, platform: any):  # type: ignore
    if(platform == 'Windows'):
        print("⚠️ You are in windows, use the scripts .bat or use the terminal bash to use files .sh")
        time.sleep(5)
    # Crear los archivos de creacion para los dos sistemas
    # operativos, por si se hace una migracion a una diferente donde se creo
    os.mkdir(f"{pwd}/scripts/unix")
    os.mkdir(f"{pwd}/scripts/windows")
    # Sistemas basados en unix
    for folder in folders:
        os.mkdir(f"{pwd}/scripts/unix/{folder}")
        time.sleep(0.2)
        file = open(f"{pwd}/scripts/unix/{folder}/create.sh", "w")
        file.write(scriptFolderUnix[folder])
        file.close()

    # Sistemas basados en windows
    for folder in folders:
        os.mkdir(f"{pwd}/scripts/windows/{folder}")
        time.sleep(0.2)
        # Se deja en el archivo en nombre consoleRPA.bat para poder correr el
        # aechivo desde el teminal del equipo de TP
        file = open(f"{pwd}/scripts/windows/{folder}/consoleRPA.bat", "w")
        file.write(scriptFolderUnix[folder])
        file.close()
