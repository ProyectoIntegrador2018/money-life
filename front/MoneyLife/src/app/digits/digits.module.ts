import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DigitsShowComponent } from './digits-show/digits-show.component';

@NgModule({
  declarations: [DigitsShowComponent],
  imports: [
    CommonModule
  ],
  exports: [
    DigitsShowComponent 
  ]
})
export class DigitsModule { }
