def appRoutingModule(pwd):
    file = open(f"{pwd}/src/app/app-routing.module.ts", "w")
    file.write('''import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from 'src/app/util/guards/auth.guard'

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
How to use the canActivate:
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

const routes: Routes = [
  //Main page when the app load, ex. LoginPage or HomePage or etc.
  {
    path: '',
    redirectTo: '/',
    pathMatch: 'full',
  },
  {
    path: 'unavailable',
    loadChildren: () =>
      import('./project/modules/unavailable/unavailable.module').then(
        (m) => m.UnavailableModule
      ),
  },
  {
    path: 'unauthorized',
    loadChildren: () =>
      import('./project/modules/unauthorized/unauthorized.module').then(
        (m) => m.UnauthorizedModule
      ),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
'''
               )
    file.close()
