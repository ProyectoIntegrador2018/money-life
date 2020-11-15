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
  
  
  getBody(url: string, body: any): Observable<any> {
    return this._http.get<any>(environment.apiEndPointTest + url, body);
  }
  get(url: string): Observable<any> {
    return this._http.get<any>(environment.apiEndPointTest + url);
  }
  post(url: string, body: any): any {
    return this._http.post<ServerResponse>(environment.apiEndPointTest + url, body);
  }
  put(url: string, body: any): any {
    return this._http.put<ServerResponse>(environment.apiEndPointTest + url, body);
  }
  // delete(url: string, body: any): any {
  //   return this._http.delete(environment.apiEndPointTest + url);
  // }
}
