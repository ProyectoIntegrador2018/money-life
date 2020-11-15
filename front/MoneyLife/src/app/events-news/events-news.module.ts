import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EventBannerComponent } from './event-banner/event-banner.component';
import { EventNotificationComponent } from './event-notification/event-notification.component';



@NgModule({
  declarations: [
    EventBannerComponent,
    EventNotificationComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    EventBannerComponent,
    EventNotificationComponent
  ]
})
export class EventsNewsModule { }
