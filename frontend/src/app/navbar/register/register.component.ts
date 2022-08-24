import { Component, OnInit } from '@angular/core';

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

  constructor() { }

  ngOnInit(): void {
  }

  register(): void {
    if (this.password === this.password2 && this.password && this.username && this.email){
      alert("Good")
    }
    else{
      alert("Wrong")
    }
  }

}
