import os
import time
import json

# Gestion de variables de entorno


def environment_variables(pwd: str, project_name: str):
    #os.system(f'cd {pwd} && npm i -D dotenv && npm i -D @angular-builders/custom-webpack')
    # leer el angular json y cambiar las directivas
    file = open(f"{pwd}/angular.json", 'r')
    json_file = json.loads(file.read())
    file.close()
    # Cambiar el webkit por el custom webpack
    json_file['projects'][project_name]['architect']['build']['builder'] = "@angular-builders/custom-webpack:browser"
    # Agregar en las opciones el archivo webpag config
    json_file['projects'][project_name]['architect']['build']['options']['customWebpackConfig']={"path":"src/custom-webpack.config.ts"}
    # Agregar el webpack al server
    json_file['projects'][project_name]['architect']['serve']['builder'] = "@angular-builders/custom-webpack:dev-server"

    file_json = open(f"{pwd}/angular.json", 'w')
    file_json.write(json.dumps(json_file, indent=2))
    file.close()
    
    #Crear archivo custom-webpack
    custom_webpack =  open(f"{pwd}/src/custom-webpack.config.ts", 'w')
    custom_webpack.write('''import { EnvironmentPlugin } from 'webpack';
require('dotenv').config()
/**
 * En los plugin se configuraran los nombres de las variables de entorno a usar en el servicio front,
 * por ejemplo si se tiene un url de una api, ex URLWEBSERVICE="https://...."
 * ese valor se almacena en el array que ingresa en EnvironmentPlugin
 */
module.exports = {
    plugins: [new EnvironmentPlugin(['URLWEBSERVICE'])]
}''')
    
    # Generar comandos node
    if(os.path.exists(f"{pwd}/tsconfig.app.json")):
        # agregar node al archivo
        config_file = open(f"{pwd}/tsconfig.app.json", 'w')
        config_file.write('''/* To learn more about this file see: https://angular.io/config/tsconfig. */
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/app",
    "types": [
      "@angular/localize",
      "node"
    ]
  },
  "files": [
    "src/main.ts"
  ],
  "include": [
    "src/**/*.d.ts"
  ]
}''')
        config_file.close()
        time.sleep(1)
        

        
environment_variables(
    r'C:\Users\mahechacruz.6\Desktop\Dev\angular_project_creator\test\test', 'test')
