import { Injectable } from '@angular/core';
import { User } from '../components/interfaces/user';
import { KeysDataUser } from './keys-data';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  canAcces(): boolean {
    return !!localStorage.getItem(KeysDataUser.userid) && !!localStorage.getItem(KeysDataUser.username);
  }
  getUser(): any{
    const user: User = {
      id: +localStorage.getItem(KeysDataUser.userid),
      username: localStorage.getItem(KeysDataUser.username)
    }
    return user;
  }
}
