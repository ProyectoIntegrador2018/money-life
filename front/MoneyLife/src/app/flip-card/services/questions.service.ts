import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from '../../auth/auth.service';
import { BaseService } from '../../shared/services/base.service';
import { User } from '../../components/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class QuestionsService {

  constructor(
    private base: BaseService,
    private authService: AuthService) { }

  initTurnQuestions(): Observable<any> {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id
    }
    return this.base.post(`pregunta/getPreguntas/`, body);
  }

  questionSelected(questionID: number): any {
    const user = this.authService.getUser() as User;
    const body = {
      UserID: user.id,
      PreguntaID: questionID
    }
    console.log(body);
    return this.base.put(`pregunta/afectaPreguntas/`, body);
  }

}
