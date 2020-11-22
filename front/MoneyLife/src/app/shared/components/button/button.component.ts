import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Button } from '../../interfaces/button';

@Component({
  selector: 'app-button',
  templateUrl: './button.component.html',
  styleUrls: ['./button.component.scss']
})
export class ButtonComponent implements OnInit {
  @Input() ob: Button;
  @Input() color: string;
  @Output() pressed: EventEmitter<Button> = new EventEmitter<Button>();
  

  constructor() { }

  ngOnInit(): void {
  }

  action(): void {
    this.pressed.emit(this.ob);
  }

}
