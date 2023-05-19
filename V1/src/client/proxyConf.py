def proxyConf(pwd):
    file = open(f"{pwd}/proxy.conf.json", 'w')
    file.write("""{
        "/":{
            "target": "API URL",
            "secure": false
        }
}       
"""
               )
    file.close()
