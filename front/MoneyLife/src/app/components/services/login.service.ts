import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from 'src/app/shared/services/base.service';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private base: BaseService) { }

  login(userData: any): Observable<any> {
    return this.base.getBody('users/login', userData);
  }

  register(userData: any): Observable<any> {
    const body = {
      username: userData.username,
      password: userData.password
    }
    return this.base.post('users', body);
  }
}
