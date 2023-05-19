import os


def services(pwd:str):
    # Crear un archivo de servicios ejemplo
    file = open(f"{pwd}/src/app/util/services/util.service.ts", "w")
    file.write("""import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.prod';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
//Import models if is necessary

//environment contains variables to make more safer the code, for example the url of any Api, key, etc
@Injectable({
  providedIn: 'root',
})
export class UtilService {
  url = '';
  constructor(private http: HttpClient) {}

  //get
  getInfo(): Observable<any> {
    let quieryUrl = '';
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    return this.http
      .get<any>(`${this.url}/{quieryUrl}`, options)
      .pipe((res) => res);
  }
  //post
  postInfo(info: any): Observable<any> {
    let quieryUrl = '';
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    return this.http
      .post<any>(`${this.url}/{quieryUrl}`, options, info)
      .pipe((res) => res);
  }
  //put
  putInfo(info: any): Observable<any> {
    let quieryUrl = '';
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    return this.http
      .put<any>(`${this.url}/{quieryUrl}`, options, info)
      .pipe((res) => res);
  }
  //delete
  deleteInfo(): Observable<any> {
    let quieryUrl = '';
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    return this.http
      .delete<any>(`${this.url}/{quieryUrl}`, options)
      .pipe((res) => res);
  }
  //patch
  patchInfo(): Observable<any> {
    let quieryUrl = '';
    const options = {
      headers: new HttpHeaders({
        'Content-type': 'application/json',
        accept: '*/*',
        //"Authorization":"Bearer " + "",
        //"Authorization": "Basic " + "",
        //"Cookie": "",
      }),
    };
    return this.http
      .patch<any>(`${this.url}/{quieryUrl}`, options)
      .pipe((res) => res);
  }
}        
"""
               )
    file.close()


