import { TestBed } from '@angular/core/testing';

import { HappinessService } from './happiness.service';

describe('HappinessService', () => {
  let service: HappinessService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HappinessService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
