import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-digits-show',
  templateUrl: './digits-show.component.html',
  styleUrls: ['./digits-show.component.scss']
})
export class DigitsShowComponent implements OnInit {
  @Input() name: string;
  @Input() number: string;

  constructor() { }

  ngOnInit(): void {
  }
}
