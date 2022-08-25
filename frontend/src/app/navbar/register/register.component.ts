import { Component, OnInit } from '@angular/core';

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

  constructor(private originApi: OriginAPIService) { }

  ngOnInit(): void {
  }

  register(): void {
    if (this.password === this.password2 && this.password && this.username && this.email){
      this.originApi.register(this.username, this.email, this.password).subscribe(response => {
        const jsonResponse = JSON.parse(JSON.stringify(response))
        if(response.status == 200) {
          console.log("registered successfully");
        } else {
          console.log("something went wrong");
        }
      })
    }
    else{
      alert("Wrong")
    }
  }

}
