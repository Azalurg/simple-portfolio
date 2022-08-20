import { importProvidersFrom, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { MarketComponent } from './market/market.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    data: {}
  },
  {
    path: 'market',
    component: MarketComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
