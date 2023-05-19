# Crear el nuevo programa angular
import os
import shutil
import time

from ...Archives.components.footer import footerHtml
from ...Archives.components.navbar import navbarHtml, navbarScss
from ...Archives.htmlFiles import appComponentHtml
from ...Archives.lib.appComponentTs import appComponentTs
from ...Archives.lib.authUser import authUserInterface
from ...Archives.lib.guard import authGuard, createGuard
from ...Archives.lib.readJson import jsonDts
from ...Archives.lib.routing import appRoutingModule
from ...Archives.lib.services import services
from ...Archives.lib.util import utilTs
from ...client.packageJson import package
from ...client.proxyConf import proxyConf
from ...client.scripts.scripts import scripts
# Dependencias del programa
from ..styles.styles import selectFramework


def angular(pwd: str, projectName: str, platform: str, pdwFiles: str):  # type: ignore
    # Crear el proyecto
    os.system(
        f"cd {pwd} && ng new {projectName} --style=scss -p teleperformance-rpa --routing true --skipGit=true --skipTests=true")
    time.sleep(1)
    # Instalar rimraf para poder hacer el comando clear para el build de la aplicacion
    # Crear estructura del projecto
    os.system(f"cd {pwd}/{projectName} && mkdir scripts")
    os.system(
        f"cd {pwd}/{projectName}/src/assets && mkdir images icons files background js json fonts ")
    os.system(f"cd {pwd}/{projectName}/src/app && mkdir project util")
    os.system(f"cd {pwd}/{projectName}/src/app/project && mkdir components modules common")
    os.system(f"cd {pwd}/{projectName}/src/app/util && mkdir models guards services")
    time.sleep(1)
    # Crear componentes comunes
    os.system(
        f"cd {pwd}/{projectName} && ng g c project/common/components/navbar && ng g c project/common/components/footer")
    os.system(
        f"cd {pwd}/{projectName} && ng g s util/services/util"
    )
    os.system(
        f"cd {pwd}/{projectName} && ng g module project/modules/unavailable --module app --route unavailable"
    )
    os.system(
        f"cd {pwd}/{projectName} && ng g module project/modules/unauthorized --module app --route unauthorized"
    )
    os.system(f"cd {pwd}/{projectName} && ng g class util/models/authUser")
    authUserInterface(f"{pwd}/{projectName}")
    time.sleep(1)
    selectFramework(f"{pwd}/{projectName}", projectName)
    time.sleep(1)
    # App component main
    appComponentHtml(f"{pwd}/{projectName}")
    # App navbar
    navbarHtml(f"{pwd}/{projectName}")
    navbarScss(f"{pwd}/{projectName}")
    # App footer
    footerHtml(f"{pwd}/{projectName}")
    # script de creacion de multiples componentes
    scripts(f"{pwd}/{projectName}", platform)
    services(f"{pwd}/{projectName}")
    jsonDts(f"{pwd}/{projectName}")
    appComponentTs(f"{pwd}/{projectName}")
    utilTs(f"{pwd}/{projectName}")
    package(f"{pwd}/{projectName}")
    proxyConf(f"{pwd}/{projectName}")
    # Creacion de los guards
    createGuard(f"{pwd}/{projectName}")
    authGuard(f"{pwd}/{projectName}")
    # App routing
    appRoutingModule(f"{pwd}/{projectName}")
    os.system(
        f"cd {pwd}/{projectName} && npm install rimraf jquery"
    )
    time.sleep(1)
    CGREEN = '\33[32m'
    CEND = '\033[0m'
    CYAN = '\033[96m'
    # Copiar imagenes
    iconHref = f"{pdwFiles}/src/Archives/images/TpLogo.png"
    imageHref = f"{pdwFiles}/src/Archives/images/BannerTeleperformance.png"
    iconAssets = f"{pwd}/{projectName}/src/assets/icons/TpLogo.png"
    imageAssets = f"{pwd}/{projectName}/src/assets/images/BannerTeleperformance.png"
    facebookHref = f"{pdwFiles}/src/Archives/images/icons8-facebook-48.png"
    instagramHref = f"{pdwFiles}/src/Archives/images/icons8-instagram-48.png"
    linkedinHref = f"{pdwFiles}/src/Archives/images/icons8-linkedin-48.png"
    twitterHref = f"{pdwFiles}/src/Archives/images/icons8-twitter-48.png"
    facebookAssets = f"{pwd}/{projectName}/src/assets/icons/icons8-facebook-48.png"
    instagramAssets = f"{pwd}/{projectName}/src/assets/icons/icons8-instagram-48.png"
    linkedinAssets = f"{pwd}/{projectName}/src/assets/icons/icons8-linkedin-48.png"
    twitterAssets = f"{pwd}/{projectName}/src/assets/icons/icons8-twitter-48.png"
    shutil.copyfile(imageHref, imageAssets)
    shutil.copyfile(iconHref, iconAssets)
    shutil.copyfile(facebookHref, facebookAssets)
    shutil.copyfile(instagramHref, instagramAssets)
    shutil.copyfile(linkedinHref, linkedinAssets)
    shutil.copyfile(twitterHref, twitterAssets)
    print(
        CGREEN +
        "\n To be able to use the project, it is recommended to navigate to the "
        "path where it is hosted and if you "
        "are using VS Code as editor, \n use the command " +
        CYAN + "(code .) " + CEND +
         CGREEN + "to open a new editor with the project,  "
        "\n otherwise if you use VS Code Insiders use the command " +
        CYAN + "(code-insiders .) " + CEND
        + CEND)
