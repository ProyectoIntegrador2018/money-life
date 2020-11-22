import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { Button } from 'src/app/shared/interfaces/button';

@Component({
  selector: 'app-event-notification',
  templateUrl: './event-notification.component.html',
  styleUrls: ['./event-notification.component.scss']
})
export class EventNotificationComponent implements OnInit {
  @Input() event: any;
  @Input() type: string;
  @Output() pressed: EventEmitter<Button> = new EventEmitter<Button>();
  @Output() close: EventEmitter<boolean> = new EventEmitter<boolean>();

  action: Button = {
    name: '',
    innerName: 'microEvent'
  }


  constructor() { }

  ngOnInit(): void {
  }
  erase(): void {
    this.close.emit(false);
  }
  openModal(): void {
    this.pressed.emit(this.action);
  }

}
