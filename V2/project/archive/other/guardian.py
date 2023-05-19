import os
import time
def generate_guard(pwd:str):
    os.system(f"cd {pwd} && ng generate guard util/guards/authorization/auth")
    # Una vez generado el archivo servicio
    time.sleep(5)
    file = open(f"{pwd}/util/services/example/example.service.ts", 'w')
    file.write('''import { Injectable, inject } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  CanActivate,
  RouterStateSnapshot,
  UrlTree,
  Router,
} from '@angular/router';
import { Observable } from 'rxjs';
import { Util } from 'src/app/util/util';

@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {
  private util = inject(Util);
  private router = inject(Router);

  canActivate(): boolean {
    //Si el usuario esta activo permite el uso de las rutas protegidas de lo contrario retornara un false y lo redirigira al home de la aplicacion
    if (!this.util.isLogin()) {
      this.util.goHome({})
      return false;
    }
    return true;
  }
}
''')
    file.close()