import os
import time
def generate_service(pwd:str):
    os.system(f"cd {pwd} && ng generate service util/services/example/example")
    # Una vez generado el archivo servicio
    time.sleep(5)
    file = open(f"{pwd}/util/services/example/example.service.ts", 'w')
    file.write('''import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ExampleService {
  //Inyectar la funcionalidad de http para las peticiones al servidor
  private http = inject(HttpClient);
  //Url del servicio, en este caso de puede usar una variable de entorno o usar el archivo de environments
  private restService: string = '';

  constructor() {}

  /**
   * Metodo de ejemplo para peticiones con el uso de los verbos HTTP
   * El <any> puede ser cambiado por un modelo de datos que se cree para mapear la respuesta de la peticon
   * un ejemplo puede ser Observable<Users[]> indicando que se esperar una salida tipo lista de un modelo de usuarios
   */
  method_name(info: any): Observable<any> {
    //Crear cabeceras para las peticiones
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    //El metodo post puede ser cambiado por cualquier metodo de la lista de opciones
    return this.http.post<any>(this.restService, options, info).pipe((res)=>res);
  }

  /**
   * Metodo de ejemplo para peticiones con el uso de request
   * El <any> puede ser cambiado por un modelo de datos que se cree para mapear la respuesta de la peticon
   * un ejemplo puede ser Observable<Users[]> indicando que se esperar una salida tipo lista de un modelo de usuarios
   */
  method_name_request(info: any): Observable<any> {
    //Crear cabeceras para las peticiones
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    //El metodo mas generico
    return this.http.request("GET", this.restService, {responseType:'json', body: info})
  }
}
''')
    file.close()