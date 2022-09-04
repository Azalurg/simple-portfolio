import { Component, OnInit } from '@angular/core';
import { OriginAPIService } from '../services/api/origin/origin-api.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-transactions',
  templateUrl: './transactions.component.html',
  styleUrls: ['./transactions.component.scss']
})
export class TransactionsComponent implements OnInit {

  private token: string;
  public transactions: any

  constructor(
    private originalApi: OriginAPIService,
    private cookie: CookieService
  ) { }

  ngOnInit(): void {
    this.getTransactions()
  }

  getTransactions(): void {
    this.token = this.cookie.get('token');
    this.originalApi.getTransactions(this.token).subscribe(response => {
      console.log(response.body);
    })
  }
}
