
def utilTs(pwd):
    file = open(f"{pwd}/src/app/util/util.ts", "w")
    file.write('''import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class Util {
  constructor(private router: Router) {
    console.debug('Iniciando...');
  }

  goHome(params: any) {
    this.goTo('/', params);
  }

  goUnauthorized(params: any) {
    this.goTo('/unauthorized', params);
  }

  goUnavailable(params: any) {
    this.goTo('/unavailable', params);
  }

  goTo(path: string, params: any) {
    //params is an object {id: _id}
    this.router.navigate([path], { queryParams: params });
  }

  public getCredentials(): any {
    if (window.localStorage) {
      const stored = localStorage.getItem('type-user');
      if (stored == null) {
        return null;
      } else {
        return JSON.parse(stored);
      }
    }
    return null;
  }

  //Rol verification for future pages
  isAdminRole(): boolean {
    const user = localStorage.getItem('type_user');
    let type: boolean = false
    if(user != null && user == "ROLE_ADMIN_cli_y") type = true
    if(user != null && user != "ROLE_ADMIN_cli_Y") type = false
    if(user == null) type = false
    return type
  }

  isEvalRole(): boolean {
    const user = localStorage.getItem('type_user');
    let type: boolean = false
    if(user != null && user == "ROLE_EVAL_app_x") type = true
    if(user != null && user != "ROLE_ADMIN_app_x") type = false
    if(user == null) type = false
    return type
  }

  isUserRole(): boolean {
    const user = localStorage.getItem('type_user');
    let type: boolean = false
    if(user != null && user == "ROLE_USER_type_n") type = true
    if(user != null && user != "ROLE_ADMIN_type_n") type = false
    if(user == null) type = false
    return type
  }

  isLogin(){
    return !!localStorage.getItem('token');
  }

  isLogout(){
    localStorage.removeItem('token');
    this.goTo('/login', {})
  }

}
'''
               )
    file.close()

