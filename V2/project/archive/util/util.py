# Creat archivo util

def util_file(pwd: str, project_name: str):
    file = open(f'{pwd}/{project_name}/src/app/util/util.ts', 'w')
    file.write('''import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})

export class Util {
    constructor(private router: Router) {
        console.debug('Iniciando...');
    }
    
    /*
    * Go Home: Volver al inicio del aplicativo
    * Go Unathorized: Ir a pagina de falta de privilegios
    * Go Unavailable: Pagina no existente
    * Go To: Enrutador generico para poder pasar parametros
    * Get Token: Captura del token desde el almanenado del sistema
    * Is Login: Usuario esta activo en la cuenta?
    * Is Logout: Usuario ha salido de la sesion?
    * Save Login Data: Guardar informacion del acceso y datos recurados por peticion HTTP
    * Delete Login Data: Eliminar datos de la sesion para dar manejo de seguridad por guardianes
    */
    
    goHome(params: any) {
        //params is an object, ex {id: _id}
        this.goTo('/', params);
    }

    goUnauthorized(params: any) {
        //params is an object, ex {id: _id}
        this.goTo('/unauthorized', params);
    }

    goUnavailable(params: any) {
        //params is an object, ex {id: _id}
        this.goTo('/unavailable', params);
    }

    goTo(path: string, params: any) {
        //params is an object, ex {id: _id}
        this.router.navigate([path], { queryParams: params });
    }
    
    getToken(){
        return sessionStorage.getItem('token')
    }
    
    isLogin(){
        return !!sessionStorage.getItem('token');
    }

    isLogout(){
        localStorage.clear()
        sessionStorage.clear()
        //Redireccionar al segemnto URL necesario
        this.goTo('/', {})
    }
    
    saveLoginData(info:any){}
    
    deleteLoginData(){}
}
''')
    file.close()
