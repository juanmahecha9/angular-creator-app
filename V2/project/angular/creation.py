import os
import sys
import time
import shutil

from ..archive.app.module import module_app
from ..archive.scripts.create import scripts
from ..archive.material.angular_material import material
from ..style.style import style
from ..cli.angular_json import angular_json
from ..archive.util.util import util_file
from ..archive.package.package import package
from ..archive.other.guardian import generate_guard
from ..archive.other.service import generate_service
from ..archive.other.router import router

DIRECTORIES = ['project', 'util']
SUBDIRECTORIESPROJECT = ['common', 'components', 'modules']
SUBDIRECTORIESUTIL = ['services', 'models', 'guards']
SCRIPTDIRS = ['common', 'components', 'modules',
              'services', 'models', 'guards']
ASSETSDIRECTORIES = 'images templates json fonts icons files background js'


def creation_project(pwd: str, project_name: str, theme: str):
    # Crear el proyecto
    os.system(
        f"cd {pwd} && ng new {project_name} --style=scss --prefix sr6-app --routing true --skip-tests true --skip-git true")
    time.sleep(1)
    # Crear la esctructura del proyecto
    for dir in DIRECTORIES:
        # Crear las subcarpetas
        if (dir == 'project'):
            os.system(f"cd {pwd}/{project_name}/src/app && mkdir {dir}")
            time.sleep(1)
            for subdir in SUBDIRECTORIESPROJECT:
                os.system(
                    f"cd {pwd}/{project_name}/src/app/{dir} && mkdir {subdir}")
        if (dir == 'util'):
            os.system(f"cd {pwd}/{project_name}/src/app && mkdir {dir}")
            time.sleep(1)
            for subdir in SUBDIRECTORIESUTIL:
                os.system(
                    f"cd {pwd}/{project_name}/src/app/{dir} && mkdir {subdir}")
    # Crear la carpeta de los script y utilidades de creacion
    os.system(f"cd {pwd}/{project_name} && mkdir scripts")
    time.sleep(1)
    for script in SCRIPTDIRS:
        print(f"Creando {script}")
        os.system(f"cd {pwd}/{project_name}/scripts && mkdir {script}")
        time.sleep(1)
    for script in SCRIPTDIRS:
        print(f"Creando {script} archivo .sh")
        # Crear el archivo sh
        file = open(f'{pwd}/{project_name}/scripts/{script}/create.sh', 'w')
        file.write(scripts(script))
        file.close()
    # Reescritura del archivo principal
    file = open(f'{pwd}/{project_name}/src/app/app.component.html', 'w')
    file.write('''<!--Archio HTML Principal del aplicativo-->
<div class="container">
    <router-outlet></router-outlet>
</div>
               ''')
    file.close()
    # Crear archivo de angular material
    file = open(f'{pwd}/{project_name}/src/app/material.module.ts', 'w')
    file.write(material())
    file.close()
    # Instalar estilos
    style(pwd, project_name, theme)
    # Modificar el angular Json
    angular_json(pwd, project_name)
    # Agragar Archivo util
    util_file(pwd, project_name)
    # Agregar el package.json
    package(pwd, project_name)
    # Agregar app module
    module_app(pwd, project_name)
    # Crear las carpteas de los assets
    os.system(
        f'cd {pwd}/{project_name}/src/assets && mkdir {ASSETSDIRECTORIES}')
    # Archivo de configuracion lectura de archivos json
    file = open(f'{pwd}/{project_name}/src/json.d.ts', 'w')
    file.write('''//Configurar lectura de archivos json en el proyecto
declare module "*"{
    const value: any;
    export default value;
}''')
    # Crear variables del entorno
    os.system(
        f'cd {pwd}/{project_name} && ng generate environments')
    # Instalar el uuid para poder hacer los id de las etiquetas variables
    os.system(
        f"cd {pwd}/{project_name} && npm uuid --save && npm i --save-dev @types/uuid")
    # Servicio de ejemplo
    generate_service(f"{pwd}/{project_name}")
    # Crear guardian
    generate_guard(f"{pwd}/{project_name}")
    # Archivo de rutas
    router(f"{pwd}/{project_name}")
    # Modificar dependencias
    os.system(f"cd {pwd}/{project_name} && npm audit fix --force")
    # README.md
    
