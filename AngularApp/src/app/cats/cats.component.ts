import { Component, OnInit } from '@angular/core';
import { Cat } from '../cat.model';
import { CatService } from '../cat.service';
import { Observable, throwError } from 'rxjs';

@Component({
  selector: 'app-cats',
  templateUrl: './cats.component.html',
  styleUrls: ['./cats.component.css']
})
export class CatsComponent implements OnInit {

  cats: Cat[] = [];
  error = [];

  constructor(private catService: CatService) { }

  ngOnInit() {
    this.getCats();
  }

  getCats() {
    this.catService.getCats()
      .subscribe((data) => {
        this.cats = data['cats'];
      },
        error => this.error = error);
  }
}
