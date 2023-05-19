def bootswatch(pwd, theme):
    file = open(f"{pwd}/src/styles.scss", 'a')
    file.write('@import "~bootswatch/dist/'+theme+'/variables";\n')
    file.write('@import "~bootswatch/dist/'+theme+'/bootswatch";\n')
    file.close()

