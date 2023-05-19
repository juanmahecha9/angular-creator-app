# Estilos
import os
import shutil
import time

# Modulo editado para ingreso de modulos solo ng-Bootstrap
from ...Archives.appModuleBootstrap import appModuleB
from ...Archives.appModuleDefault import appModuleDefault
# Modulo editado para ingreso de modulos solo angular material
from ...Archives.appModuleMaterial import appModuleM
# Modulo editado para ingreso de modulos angular material y ng-boostrap
from ...Archives.appModuleMaterialBoostrap import appModuleMB
from ...Archives.bootswatch import bootswatch
# Index HTML para tener los link js o no
from ...Archives.htmlFiles import indexHtml, indexHtmlBootstrap
from ...Archives.materialModules import materialModules
from ...client.angularJson import angularJson

frameworks = [
    '1. Bootstrap and Angular Material (Recommended).', '2. Bootstrap.', '3. Angular Material.']

def selectFramework(pwd, projectName):
    CRED = '\033[91m'
    CEND = '\033[0m'
    framework = input('Do you want use any style framework? y/N -> ')
    if framework.lower() == 'y':
        print('Which of these selections would you like to install?... \n')
        for framework in frameworks:
            print(CRED + framework + "\n" + CEND)
        time.sleep(1)

        selected = input('Select only the number, ex. 1 -> ')

        if selected == '1':
            print("\n Installing Angular Material and Bootstrap")
            bootstrap(pwd)
            material(pwd)
            appModuleMB(pwd)
            indexHtmlBootstrap(pwd, projectName)
            angularJson(pwd, projectName, 'y')
        if selected == '2':
            print('\n Installing Bootstrap and ng-bootstrap')
            bootstrap(pwd)
            appModuleB(pwd)
            indexHtmlBootstrap(pwd, projectName)
            angularJson(pwd, projectName, 'y')
        if selected == '3':
            print('\n Installing Angular Material')
            material(pwd)
            appModuleM(pwd)
            indexHtml(pwd, projectName)
            angularJson(pwd, projectName, 'n')
    else:
        appModuleDefault(pwd)
        angularJson(pwd, projectName, 'n')
        print("Continue!")

# Definiciones
def material(pwd):
    os.system(f"cd {pwd} && ng add @angular/material")
    # importar los modulos de material
    materialModules(pwd)

def bootstrap(pwd):
    themes = [
        'cerulean',
        'cosmo',
        'cyborg',
        'darkly',
        'flatly',
        'journal',
        'litera',
        'lumen',
        'lux',
        'materia',
        'minty',
        'morph',
        'pulse',
        'quartz',
        'sandstone',
        'simplex',
        'sketchy',
        'slate',
        'solar',
        'spacelab',
        'superhero',
        'united',
        'vapor',
        'yeti',
        'zephyr'
    ]
    print('Select the bootstrap theme: ')
    print('You can see the themes in this URL: https://bootswatch.com/')
    themeSelected = input('Enter the name of the style selected, ex. Materia \n -> ')
    if(themeSelected.lower() in themes):
        print(f'update theme with {themeSelected}...')
        theme = themeSelected.lower()
    else:
        print('Theme is not valid, update to default theme: cosmo')
        theme = 'cosmo'
    os.system(f"cd {pwd} && ng add @ng-bootstrap/ng-bootstrap")
    os.system(f"cd {pwd} && npm i bootswatch")
    time.sleep(1)        
    bootswatch(pwd, theme)
