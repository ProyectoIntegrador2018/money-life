import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ServerResponse } from '../interfaces/server-response';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BaseService {
  constructor(private _http: HttpClient) { }
  
  get(url: string): Observable<any> {
    return this._http.get<ServerResponse>(environment.apiEndPoint + url);
  }
  post(url: string, body: any): any {
    return this._http.post<ServerResponse>(environment.apiEndPoint + url, body);
  }
  put(url: string, body: any): any {
    return this._http.put<ServerResponse>(environment.apiEndPoint + url, body);
  }
  // delete(url: string, body: any): any {
  //   return this._http.delete(environment.apiEndPoint + url);
  // }
}
