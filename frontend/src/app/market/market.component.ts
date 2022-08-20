import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { CoingeckoService } from '../services/coingecko.service';
import { MatPaginator, MatPaginatorIntl} from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { ChangeDetectorRef } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';

interface Coin{
  id: string,
  name: string,
  image: string
}

@Component({
  selector: 'app-market',
  templateUrl: './market.component.html',
  styleUrls: ['./market.component.scss']
})

export class MarketComponent implements OnInit {
  private subtitleCollection = ["Is the market going nuts now?", "Go, make money!!!"];
  public subtitle = "";
  public displayedColumns: string[] = ['position' ,'name', 'current_price', 'price_change_percentage_24h','market_cap'];
  public dataSource: any;
  public pageSize = 50

  @ViewChild(MatPaginator) paginator !: MatPaginator;
  @ViewChild(MatSort) sort !: MatSort;
  
  constructor(private service:CoingeckoService) {}

  ngOnInit(): void {
    this.choseSubtitle();

    this.service.getCoins('usd', 100).subscribe(response => {
      const data: any = response 
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    })
    
    if (window.screen.availWidth < 800){
      this.displayedColumns = this.displayedColumns.slice(1, 3)
      this.pageSize = 10
    }
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue;

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  choseSubtitle(): void {
    this.subtitle = this.subtitleCollection[Math.floor(Math.random() * this.subtitleCollection.length)];
  }
}
