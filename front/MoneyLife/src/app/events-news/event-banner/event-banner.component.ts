import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-event-banner',
  templateUrl: './event-banner.component.html',
  styleUrls: ['./event-banner.component.scss']
})
export class EventBannerComponent implements OnInit {
  @Input() msg: any;

  constructor() { }

  ngOnInit(): void {
    if (!this.msg) {
      this.msg = "No hay noticias";
    }
  }
}
