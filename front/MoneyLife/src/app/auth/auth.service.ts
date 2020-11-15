import { Injectable } from '@angular/core';
import { User } from '../components/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  canAcces(): boolean {
    return !!localStorage.getItem('userId');
  }
  getUser(): any{
    const user: User = {
      id: +localStorage.getItem('userID'),
      username: localStorage.getItem('username')
    }
    return user;
  }
}
