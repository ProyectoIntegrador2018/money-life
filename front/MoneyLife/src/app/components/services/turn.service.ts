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
  
  getUser(): any {
    const user = this.authService.getUser() as User;
    return {
      UserID: user.id
    }
  }

  initTurn(): Observable<any> { // Called at the start of a new turn
    return this.base.post(`turno/inicio/`, this.getUser());
  }
  
  refreshTurn(): Observable<any> {
    return this.base.post(`turno/intermedio/`, this.getUser());
  }
  financialPortfolio(): Observable<any> {
    return this.base.post(`portafolio/financiero/`, this.getUser());

  }
  eraseGame(): Observable<any> {
    return this.base.put(`terminar/juego/`, this.getUser());
  }
}
