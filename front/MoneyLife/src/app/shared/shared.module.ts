import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ModalComponent } from './components/modal/modal.component';
import { ButtonComponent } from './components/button/button.component';



@NgModule({
  declarations: [
    ModalComponent, 
    ButtonComponent,
  ],
  imports: [
    CommonModule
  ],
  exports: [
    ModalComponent,
    ButtonComponent
  ]
})
export class SharedModule { }
