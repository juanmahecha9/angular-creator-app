import json


def angularJson(pwd: str, projectName: str, frameworkStyle: str):
    scripts = [
        "node_modules/jquery/dist/jquery.min.js",
        "node_modules/bootstrap/dist/js/bootstrap.min.js",
        "node_modules/@popperjs/core/dist/umd/popper.min.js",
    ]
    with open(f'{pwd}/angular.json', 'r') as file_:
        jsonLines = json.loads(str(file_.read()))
        jsonLines['projects'][f'{projectName}']['architect']['build']['options']['baseHref'] = '/application'
    if(frameworkStyle == 'y'):
        jsonLines['projects'][f'{projectName}']['architect']['build']['options']['scripts'] = scripts

    file = open(f"{pwd}/angular.json", 'w')
    file.write(json.dumps(jsonLines, indent=4))
    file.close()
