import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BaseService {

  constructor(private _http: HttpClient) { }
  get(url: string): Observable<any> {
    console.log(environment.apiEndpoint + url);
    return this._http.get<any>(environment.apiEndpoint + url);
  }
  post(url: string, body: any): any {
    return this._http.post<any>(environment.apiEndpoint + url, body);
  }
  put(url: string, body: any): any {
    return this._http.put<any>(environment.apiEndpoint + url, body);
  }
  delete(url: string, body: any): any {
    return this._http.delete(environment.apiEndpoint + url);
  }
}
