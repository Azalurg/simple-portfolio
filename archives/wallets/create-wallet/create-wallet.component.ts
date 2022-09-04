import { Component, Input } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { OriginAPIService } from 'src/app/services/api/origin/origin-api.service';
import { ToastrService } from 'ngx-toastr';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-create-wallet',
  templateUrl: './create-wallet.component.html',
  styleUrls: ['./create-wallet.component.scss']
})
export class CreateWalletComponent {
  public token!: string;
  public name: string = "";

  constructor(
    private dialog: MatDialog,
    private toastr: ToastrService,
    private originApi: OriginAPIService,
    private cookie: CookieService) { }

  createWallet(): void {
    this.token = this.cookie.get('token')
    this.originApi.createWallets(this.token, this.name).subscribe(response => {
      if(response.status == 200) {
        this.toastr.success('Wallet created', 'Wallets')
        this.dialog.closeAll()
        window.location.reload();
      } else {
        this.toastr.error('Something went wrong...', 'Wallets')
      }
    })
    this.dialog.closeAll()
  }

}
