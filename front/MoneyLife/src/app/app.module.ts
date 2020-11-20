import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule, HTTP_INTERCEPTORS } from '@angular/common/http';
/** Authification guard */
import { AuthService } from './auth/auth.service';
/** Components */
import { LoginComponent } from './components/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { MainMenuComponent } from './components/main-menu/main-menu.component';
/** Modules*/
import { FlipCardModule } from './flip-card/flip-card.module';
import { EventsNewsModule } from './events-news/events-news.module';
import { HappinessModule } from './happiness/happiness.module';
import { DigitsModule } from './digits/digits.module';
import { BoxModule } from './box/box.module';
import { LoanModule } from './loan/loan.module';
import { SharedModule } from './shared/shared.module';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    MainMenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    FlipCardModule,
    EventsNewsModule,
    HappinessModule,
    DigitsModule,
    BoxModule,
    LoanModule,
    SharedModule,
  ],
  providers: [
    AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
