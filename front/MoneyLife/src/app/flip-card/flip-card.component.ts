import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'flip-card',
  templateUrl: './flip-card.component.html',
  styleUrls: ['./flip-card.component.scss']
})
export class FlipCardComponent implements OnInit {
  toggleProperty = false;
  @Output() selected: EventEmitter<boolean> = new EventEmitter<boolean>();

  constructor() { }

  ngOnInit(): void {
  }

  toggle(): void {
    this.toggleProperty = !this.toggleProperty;
  }
  sendData(): void {
    this.selected.emit(true);
  }
}
