import os
import json

# Modificar el archivo package.json, agregando los scripts de ejecucion necesario


def package(pwd: str, project_name: str):
    os.system(f'cd {pwd}/{project_name} && npm install rimraf --save')
    file = open(f'{pwd}/{project_name}/package.json', 'r') 
    pkg = json.loads(file.read())
    file.close()
    pkg['scripts']['start'] = "ng serve --port 4200"
    pkg['scripts']['clean'] = "rimraf dist"
    pkg['scripts']['build'] = "npm run clean && ng build --allowed-common-js-dependencies --common-chunk --progress --base-href /application/ --deploy-url /application/"
    pkg['scripts']['buildazure'] = "npm run clean && ng build"
    
    new = open(f'{pwd}/{project_name}/package.json', 'w') 
    new.write(json.dumps(pkg, indent=2))
    new.close()
    
    
    
    
