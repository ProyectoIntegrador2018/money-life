import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-event-notification',
  templateUrl: './event-notification.component.html',
  styleUrls: ['./event-notification.component.scss']
})
export class EventNotificationComponent implements OnInit {
  @Input() msg: string;
  @Input() type: string;
  @Output() close: EventEmitter<boolean> = new EventEmitter<boolean>();

  constructor() { }

  ngOnInit(): void {
  }
  erase(): void {
    this.close.emit(false);
  }

}
