import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoingeckoService {
  
  constructor(private httpClient: HttpClient) { }

  getCoins(vs_currency: string = "usd", amount: number = 100, pages: number = 1, price_change_percentage: string = '1h, 24h, 7d') {
    const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=${vs_currency}&per_page=${amount}&page=${pages}&price_change_percentage${price_change_percentage}`;
    return this.httpClient.get(url);
  }
}
