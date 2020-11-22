import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Button } from 'src/app/shared/interfaces/button';

@Component({
  selector: 'app-box',
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.scss']
})
export class BoxComponent implements OnInit {
  @Output() act: EventEmitter<boolean> = new EventEmitter<boolean>();
  active = false;
  newTurn: Button = {
    name: 'Nuevo turno',
    innerName: ''
  };
  constructor() { }

  ngOnInit(): void {
  }
  activateBox(): void {
    this.active = true;
    this.act.emit(false);
    setTimeout(_ => {
      this.active = false;
    }, 1000);
  }

}
