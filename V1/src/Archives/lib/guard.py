import os
import time


def createGuard(pwd):
    print(
        "This guard is for protect the routes when the user is not login into the app, CHOOSE THE OPTION => CanActivate ")
    time.sleep(5)
    os.system(
        f"cd {pwd} && npx ng g guard util/guards/auth")


def authGuard(pwd):
    file = open(f"{pwd}/src/app/util/guards/auth.guard.ts", "w")
    file.write('''import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { Util } from 'src/app/util/util';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  //Protect the routes when is not login
  
  constructor(private utilService: Util, private router: Router) { }
  
  canActivate():boolean{
    if (this.utilService.isLogin()){
      return true;
    }else{
      this.router.navigate(['/login']);
      return false;
    }
  }
  
}
'''
               )
    file.close()
