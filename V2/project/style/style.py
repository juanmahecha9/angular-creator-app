import os
import time

def style(pwd: str, project_name: str, theme: str):
    # Instalar bootstrap bootswatch ng-bootstrap
    os.system(f"cd {pwd}/{project_name} && ng add @ng-bootstrap/ng-bootstrap")
    os.system(f"cd {pwd}/{project_name} && npm i bootswatch")
    # Editar el archivo css del programa
    file = open(f'{pwd}/{project_name}/src/styles.scss', 'w')
    file.write(f'''/* You can add global styles to this file, and also import other style files */
// Import Bootstrap
/* Importing Bootstrap SCSS file. */
@import 'bootstrap/scss/bootstrap';
@import "~bootswatch/dist/{theme}/variables";
@import "~bootswatch/dist/{theme}/bootswatch";
''')
    file.close()
    # Instalar Angular material
    time.sleep(2)
    os.system(f"cd {pwd}/{project_name} && ng add @angular/material")
