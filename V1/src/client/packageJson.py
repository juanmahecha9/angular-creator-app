import json


def package(pwd):
    with open(f'{pwd}/package.json', 'r') as file_:
        jsonLines = json.loads(str(file_.read()))
        jsonLines['scripts'] = {
            "start": "ng serve --port 4200",
            "clean": "rimraf dist",
            "build": "npm run clean && ng build ",
            "watch": "ng build --watch --configuration development",
            "buildStaticApp": "npm run clean  && ng build --base-href /static/",
        }

    file = open(f"{pwd}/package.json", 'w')
    file.write(json.dumps(jsonLines, indent=4))
    file.close()



