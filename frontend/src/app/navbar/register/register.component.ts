import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"
import { ToastrService } from 'ngx-toastr';
import { MatDialog } from '@angular/material/dialog';

import { OriginAPIService } from 'src/app/services/api/origin/origin-api.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  username: string = "";
  password: string = "";
  password2: string = "";
  email: string = "";

  constructor(
    private originApi: OriginAPIService,
    private router: Router,
    private toastr: ToastrService,
    private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  register(): void {
    if (this.password !== this.password2){
      this.toastr.error('Passwords mast by the same', 'Register')
      return
    }

    if (this.username.length < 2 && this.email.length < 2){
      this.toastr.error('Username / Email too short', 'Register')
      return
    }

    if (this.password.length < 8){
      this.toastr.error('Password is too short! (minimum 8 chars)', 'Register')
      return
    }

    this.originApi.register(this.username, this.email, this.password).subscribe(response => {
      // const jsonResponse = JSON.parse(JSON.stringify(response))
      if(response.status == 200) {
        this.toastr.success('Registered successfully', 'Register')
        this.dialog.closeAll()
        this.router.navigate(['/'])
      } else {
        this.toastr.error('Something went wrong', 'Register')
      }
    })
  }
}
