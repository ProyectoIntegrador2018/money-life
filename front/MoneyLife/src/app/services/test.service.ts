import { Injectable } from '@angular/core';
import { BaseService } from '../services/base.service';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private base: BaseService) { }

  getEvent(): any{
    return this.base.get('evento/inicioTurno/');
  }

  putEvent(body): any{
    return this.base.put('evento/afectaTurno/', body)
  }

  getTurno(): any{
    return this.base.get('')
  }

}
