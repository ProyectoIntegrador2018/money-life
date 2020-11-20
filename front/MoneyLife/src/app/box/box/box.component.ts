import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-box',
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.scss']
})
export class BoxComponent implements OnInit {
  @Output() act: EventEmitter<boolean> = new EventEmitter<boolean>();
  active = false;

  constructor() { }

  ngOnInit(): void {
  }
  activateBox(): void {
    this.act.emit(false);
    this.active = true;
    setTimeout(_ => {
      this.active = false;
      this.act.emit(true);
    }, 2000);
  }

}
