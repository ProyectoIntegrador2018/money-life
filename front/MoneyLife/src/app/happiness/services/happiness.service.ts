import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../../auth/auth.service';
import { BaseService } from '../../shared/services/base.service';
import { User } from '../../components/interfaces/user';


@Injectable({
  providedIn: 'root'
})
export class HappinessService {

  constructor(
    private base: BaseService,
    private authService: AuthService) { }
  
  getUser(): any {
    const user = this.authService.getUser() as User;
    return {
      UserID: user.id
    }
  }
  getHappiness(): Observable<any> {
    return this.base.post(`turno/felicidad/`, this.getUser())
  }
}
  