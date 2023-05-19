import json


def angular_json(pwd: str, project_name: str):
    file = open(f'{pwd}/{project_name}/angular.json', 'r')
    angular_config_json = json.loads(file.read())
    file.close()
    # Modificar el archivo angular.json para agragar las dependiencias necesarias de boostrap
    angular_config_json['projects'][project_name]['architect']['build']['options']['styles'] = [
        "node_modules/bootstrap/dist/css/bootstrap.min.css", "src/styles.scss"]
    angular_config_json['projects'][project_name]['architect']['build']['options']['scripts'] = [
        "node_modules/bootstrap/dist/js/bootstrap.js"]
    # Agregar la base del proyecto
    angular_config_json['projects'][project_name]['architect']['build']['options']['baseHref'] = "/application"
    # Guardar cambios
    file_save = open(f'{pwd}/{project_name}/angular.json', 'w')
    file_save.write(json.dumps(angular_config_json, indent=2))
    file_save.close()
