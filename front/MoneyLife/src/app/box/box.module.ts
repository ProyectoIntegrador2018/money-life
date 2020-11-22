import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BoxComponent } from './box/box.component';
import { SharedModule } from 'src/app/shared/shared.module';

@NgModule({
  declarations: [BoxComponent],
  imports: [
    CommonModule,
    SharedModule
  ],
  exports: [
    BoxComponent
  ]
})
export class BoxModule { }
