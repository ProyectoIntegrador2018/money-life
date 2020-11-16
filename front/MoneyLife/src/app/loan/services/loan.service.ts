import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../../auth/auth.service';
import { BaseService } from '../../shared/services/base.service';
import { User } from '../../components/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class LoanService {

  constructor(
    private base: BaseService,
    private authService: AuthService) { }

  getUser(): any {
    const user = this.authService.getUser() as User;
    return {
      UserID: user.id
    };
  }
  
  getCatalogue(): Observable<any> {
    return this.base.post(`prestamo/catalogo/`, '');
  }

  selectedLoan(loanID: number, totalValue: number, hitch: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      PrestamoID: loanID,
      ValorTotal: totalValue,
      Enganche: hitch
    } 
    return this.base.put(`prestamo/Realizar/`, body);    
  }

  seeMyLoans(): Observable<any> {
    return this.base.post(`prestamo/prestamosActuales/`, this.getUser());
  }
  
  payLoan(loanID: number, qty: number): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      PrestamoID: loanID,
      Amortizacion: qty
    } 
    return this.base.put(`prestamo/Amortizacion/`, body);
  }
}
