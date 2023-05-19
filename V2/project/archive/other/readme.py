def readme(pwd: str, project_name:str):
    file = open(f"{pwd}/README.md", 'w')
    file.write(f'''# Projecto {project_name}
Interfaz grafica Custom para proyectos creados  con el uso del framework Angular

## Comandos de ejecucion
- Ejecutar el desarrollo: usar npm run start
- Compilar el desarrollo para uso en servidores IIS: usar npm run build
- Compilar el desarrollo para uso en azure o google cloud: usar npm run buildazure
- Eliminar carpeta dist actual: usar npm run clean

Si se llega a usar dependencias antiguas o versiones de angular inferiores a la 13
- Instalar las dependiencias: usar npm install --legacy-peer-deps
- Ejecutar el servicio: usar set NODE_OPTIONS=--openssl-legacy-provider && ng serve

# Como incluir variables de entorno en el desarrollo
se requiere crear un archivo .env dentro del desarrollo, en el cual se tendran los datros sensibles para el manejo como llaves, tokens, url, entre otros
''')
