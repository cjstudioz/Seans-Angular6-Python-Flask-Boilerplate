import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule  } from '@angular/common/http';

import { AppComponent } from './app.component';
import { CatsComponent } from './cats/cats.component';
import { DogsComponent } from './dogs/dogs.component';
import { BirdsComponent } from './birds/birds.component';
import { HomeComponent } from './home/home.component';

import { routingModule } from './app.routing';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { OkCancelComponent } from './ok-cancel/ok-cancel.component';

@NgModule({
  declarations: [
    AppComponent,
    CatsComponent,
    DogsComponent,
    BirdsComponent,
    HomeComponent,
    OkCancelComponent
  ],
  imports: [
    BrowserModule,
    routingModule,
    NgbModule.forRoot(),
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
