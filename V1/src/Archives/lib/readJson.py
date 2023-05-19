import os


def jsonDts(pwd):
    # Crear un archivo de servicios ejemplo
    file = open(f"{pwd}/src/json.d.ts", "w")
    file.write("""//Configuration to be able to read JSON file
declare module "*"{
    const value: any;
    export default value;
}       
"""
               )
    file.close()
