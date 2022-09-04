import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router"
import { ToastrService } from 'ngx-toastr';
import { MatDialog } from '@angular/material/dialog';
import { CookieService } from 'ngx-cookie-service';

import { OriginAPIService } from 'src/app/services/api/origin/origin-api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  username: string = "";
  password: string = "";

  constructor(
    private originApi: OriginAPIService,
    private router: Router,
    private toastr: ToastrService,
    private dialog: MatDialog,
    private cookie: CookieService) { }

  ngOnInit(): void {
  }

  login(): void {
    this.originApi.login(this.username, this.password).subscribe(response => {
      const jsonResponse = JSON.parse(JSON.stringify(response))
      if(response.status == 200) {
        this.cookie.set('token', jsonResponse.body.token, 0.05)
        this.toastr.success('Login successfully', 'Login')
        this.dialog.closeAll()
        this.router.navigate(['/'])
      } else {
        this.toastr.error('Wrong username or password', 'Login')
      }
    })
  }


}
