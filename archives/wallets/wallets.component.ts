import { Component, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { OriginAPIService } from '../services/api/origin/origin-api.service';
import { CookieService } from 'ngx-cookie-service';
import { ToastrService } from 'ngx-toastr';
import { Router } from "@angular/router"
import { CreateWalletComponent } from './create-wallet/create-wallet.component';
import { MatDialog } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { Wallet } from '../common/called/wallet';

@Component({
  selector: 'app-wallets',
  templateUrl: './wallets.component.html',
  styleUrls: ['./wallets.component.scss']
})
export class WalletsComponent implements OnInit {

  private token: string;
  public wallets: Observable<Wallet[]>;
  public selectedValue!: string;
  public selectedWallet: object ;

  constructor(
    private originalApi: OriginAPIService,
    private cookie: CookieService,
    private dialogRef: MatDialog,
    private toastr: ToastrService,
    private router: Router) { }

  ngOnInit(): void {
    this.getWallets()
  }

  createWallet(): void {
    this.dialogRef.open(CreateWalletComponent)
  }

public getWallets(): void {
  this.token = this.cookie.get('token');
  if (this.token) {
    this.originalApi.getWallets(this.token).subscribe(response => {
      const jsonResponse = JSON.parse(JSON.stringify(response))
      if (response.status == 200) {
        this.wallets = jsonResponse.body
        console.log(this.wallets);
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
