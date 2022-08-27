import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { MaterialModule } from '../material-module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CustomMaterialModule } from './common/material-modules/material-modules.module';
import { ToastrModule } from 'ngx-toastr';
import { CookieService } from 'ngx-cookie-service';

import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { LogoComponent } from './common/logo/logo.component';
import { MarketComponent } from './market/market.component';
import { LoginComponent } from './navbar/login/login.component';
import { RegisterComponent } from './navbar/register/register.component';
import { WalletsComponent } from './wallets/wallets.component';
import { ProfileComponent } from './profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavbarComponent,
    FooterComponent,
    LogoComponent,
    MarketComponent,
    LoginComponent,
    RegisterComponent,
    WalletsComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    CustomMaterialModule,
    ToastrModule.forRoot({
      timeOut: 4000,
      progressBar:true,
      progressAnimation: 'decreasing',
      preventDuplicates: true
    })
  ],
  providers: [
    CookieService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
