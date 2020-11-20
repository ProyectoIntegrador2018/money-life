import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../../auth/auth.service';
import { BaseService } from '../../shared/services/base.service';
import { User } from '../../components/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class ActionsService {

  constructor(
    private base: BaseService,
    private authService: AuthService
  ) { }

  getUser(): any {
    const user = this.authService.getUser() as User;
    return {
      UserID: user.id
    };
  }
  getCatalogue(): Observable<any> {
    return this.base.post(`inversion/catalogoDisponibles/`, this.getUser());
  }

  investToNewAction(actionID: number, qty: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      InversionID: actionID,
      Cantidad: qty
    };
    return this.base.post(`inversion/nueva/`, body);
  }

  myActions(): Observable<any> {
    return this.base.post(`inversion/inversionesActuales/`, this.getUser());
  }

  investToOwnAction(actionID: number, qty: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      InversionID: actionID,
      Cantidad: qty
    };
    return this.base.put(`inversion/agregarDinero/`, body);
  }
  getMoneyFromAction(actionID: number, qty: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      InversionID: actionID,
      Cantidad: qty
    };
    return this.base.put(`inversion/retirarDinero/`, body);
  }
  sellAction(actionID: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      InversionID: actionID,
    };
    return this.base.put(`inversion/retirarAccion/`, body);
  }
  myOwnInvestmentFromQuestions(): Observable<any> {
    return this.base.post(`inversion/inversionesPersonalesActuales/`, this.getUser());
  }
  sellOwnInvestments(actionID: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      InversionID: actionID,
    };
    return this.base.put(`inversion/retirarInversionPersonal/`, body)
  }
}
