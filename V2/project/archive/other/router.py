import os
import time
def router(pwd:str):
    
    # Una vez generado el archivo servicio
    time.sleep(5)
    file = open(f"{pwd}/src/app/app-routing.module.ts", 'w')
    file.write('''import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//importar guardian
import { AuthGuard } from './util/guards/authorization/auth.guard';

/*
How to set a new route:
In routes set:
{
  path: "_urlSegment",
  component: _component,
}
In this case is a public route.
*/

/*
How to use thecanActivate:
In routes set:
{
  path: "_urlSegment",
  component: _component,
 canActivate: [AuthGuard],
}
*/

/*
How to redirect to unavailable page:
In the end of the array routes, set the next condition:
{ path: "**", redirectTo: "/unavailable" },
*/

const routes: Routes = [];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

''')
    file.close()