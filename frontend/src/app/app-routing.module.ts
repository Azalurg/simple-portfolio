import { importProvidersFrom, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { MarketComponent } from './market/market.component';
import { ProfileComponent } from './profile/profile.component';
import { WalletsComponent } from './wallets/wallets.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    data: {}
  },
  {
    path: 'market',
    component: MarketComponent
  },
  {
    path: 'wallets',
    component: WalletsComponent
  },
  {
    path: 'profile',
    component: ProfileComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
