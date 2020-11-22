import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-event-banner',
  templateUrl: './event-banner.component.html',
  styleUrls: ['./event-banner.component.scss']
})
export class EventBannerComponent implements OnInit {
  @Input() event: any;

  constructor() { }

  ngOnInit(): void {
  }
}
