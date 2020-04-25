import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../Vacancy';
import { ControlDataService } from '../control-data.service';

@Component({
  selector: 'app-top-vacancies',
  templateUrl: './top-vacancies.component.html',
  styleUrls: ['./top-vacancies.component.css']
})
export class TopVacanciesComponent implements OnInit {
  VacanciesTop: Vacancy[];

  constructor(private service: ControlDataService) { }

  ngOnInit(): void {
    this.getTopVacancies();
  }

  getTopVacancies(): void {
    this.service.getTopVacancies()
      .subscribe(VacanciesTop => this.VacanciesTop = VacanciesTop);
  }
}
