import { TestBed } from '@angular/core/testing';

import { InitTurnService } from './init-turn.service';

describe('InitTurnService', () => {
  let service: InitTurnService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InitTurnService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
