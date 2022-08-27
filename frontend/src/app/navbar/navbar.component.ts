import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(
    private dialogRef: MatDialog,
    private cookie: CookieService) { }

  ngOnInit(): void {
  }

  isLogin(): boolean {
    if (this.cookie.get('token')){
      return true
    }
    return false
  }

  login(){
    this.dialogRef.open(LoginComponent)
  }

  register(){
    this.dialogRef.open(RegisterComponent)
  }

  logout() {
    this.cookie.delete('token')
  }
}
