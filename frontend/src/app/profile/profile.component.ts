import { Component, OnInit } from '@angular/core';
import { OriginAPIService } from '../services/api/origin/origin-api.service';
import { CookieService } from 'ngx-cookie-service';
import { ToastrService } from 'ngx-toastr';
import { Router } from "@angular/router"


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  private token: string;
  public user: any

  constructor(
    private originalApi: OriginAPIService,
    private cookie: CookieService,
    private toastr: ToastrService,
    private router: Router) { }

  ngOnInit(): void {
    this.token = this.cookie.get('token');
    if (this.token) {
      this.originalApi.getUser(this.token).subscribe(response => {
        const jsonResponse = JSON.parse(JSON.stringify(response))
        if (response.status == 200) {
          this.user = jsonResponse.body
        } else {
          this.toastr.error('Wrong token!!!', 'Profile')
          this.router.navigate(['/'])
        }
      })
    } else {
      this.router.navigate(['/'])
    }
  }

}
