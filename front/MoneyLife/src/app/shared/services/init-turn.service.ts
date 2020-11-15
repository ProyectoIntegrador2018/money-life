import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../../auth/auth.service';
import { BaseService } from '../../shared/services/base.service';
import { User } from '../../components/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class InitTurnService {

  constructor(
    private base: BaseService,
    private authService: AuthService) { }

  initTurn(): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id
    }
    return this.base.getBody(`turno/inicio`, body);
  }
}
