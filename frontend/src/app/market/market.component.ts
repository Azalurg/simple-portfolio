import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-market',
  templateUrl: './market.component.html',
  styleUrls: ['./market.component.scss']
})
export class MarketComponent implements OnInit {
  private subtitleCollection = [
    "Is the market going nuts now?",
    "Go, make money!!!"
  ];
  public subtitle = "";
  
  constructor() { }

  ngOnInit(): void {
    this.choseSubtitle();
  }

  choseSubtitle(): void {
    this.subtitle = this.subtitleCollection[Math.floor(Math.random() * this.subtitleCollection.length)];
  }
}
