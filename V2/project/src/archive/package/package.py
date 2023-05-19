import json

def pck(pwd: str):
    file = open(f"{pwd}/api/package.json","r")
    pkg = json.loads(file.read())
    file.close()
    
    pkg['scripts']['init'] = 'tsc'
    pkg['scripts']['start'] = 'node dist/index.js'
    pkg['scripts']['dev'] = 'nodemon src/index.ts --exec ts-node'
    pkg['scripts']['build'] = 'npm run init'
    new = open(f"{pwd}/api/package.json","w")
    new.write(json.dumps(pkg, indent=2))
    new.close()
    


