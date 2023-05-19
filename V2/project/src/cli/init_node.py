import os
import time

from ..archive.package.package import pck
from ..archive.tsconfig.tsconfig import tsconfig

def creartion_project_node(pwd: str):
    # Crear la carpeta
    print("PWD:", pwd)
    os.system(f"cd {pwd} && mkdir api")
    os.system(f"cd {pwd}/api && npm init -y")
    # Instlar aplicativos y dependencias
    lib_dev = 'npm install @types/base-64 @types/cors @types/express @types/jsonwebtoken @types/morgan @types/mssql @types/nodemailer @types/request @types/sequelize concurrently nodemon ts-node ts-node-dev typescript @types/dotenv @types/md5  -D'
    lib_save = "npm install  axios base-64 cors crypto dotenv express fs generate-password jsonwebtoken md5 morgan mssql nodemailer request rimraf sequelize sequelize-typescript tedious ts-dotenv --save"
    os.system(f"cd {pwd}/api && {lib_dev} && {lib_save}")
    time.sleep(1)
    # Iniciarlizar el package json
    pck(pwd)
    # Inicializar proyecto con typescript
    os.system(f'cd {pwd}/api && npm run init -- --init')
    tsconfig(pwd)
    #Crear estructura del proyecto
    os.system(f"cd {pwd}/api && mkdir src")
    os.system(f"cd {pwd}/api/src && mkdir config controller database email lib helper models private public report routes service")
    