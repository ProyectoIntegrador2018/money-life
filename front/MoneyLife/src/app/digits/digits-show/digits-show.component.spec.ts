import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DigitsShowComponent } from './digits-show.component';

describe('DigitsShowComponent', () => {
  let component: DigitsShowComponent;
  let fixture: ComponentFixture<DigitsShowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DigitsShowComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DigitsShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
