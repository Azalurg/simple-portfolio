import { Component, OnInit } from '@angular/core';

import { OriginAPIService } from 'src/app/services/api/origin/origin-api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  username: string = "";
  password: string = "";

  constructor(private originApi: OriginAPIService) { }

  ngOnInit(): void {
  }

  login(): void {
    this.originApi.login(this.username, this.password).subscribe(response => {
      const jsonResponse = JSON.parse(JSON.stringify(response))
      if(response.status == 200) {
        console.log(jsonResponse.body.token);
        console.log("registered successfully");
      } else {
        console.log("something went wrong");
      }
    })
  }


}
