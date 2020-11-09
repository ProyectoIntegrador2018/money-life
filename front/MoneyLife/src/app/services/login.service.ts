import { Injectable } from '@angular/core';
import { BaseService } from '../services/base.service';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private base: BaseService) { }

  postRegister(userData){
    return this.base.post('users/', userData)
  }

  onLogin(userData){
    return this.base.post('api-auth/', userData)
  }

}
