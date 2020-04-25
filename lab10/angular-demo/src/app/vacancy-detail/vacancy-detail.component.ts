import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../Vacancy';
import { ControlDataService } from '../control-data.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Company } from '../Company';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-vacancy-detail',
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {
  vacancy: Vacancy;
  formVacancy: FormGroup;
  formUpdateShow = false;

  constructor(
    private service: ControlDataService,
    private route: ActivatedRoute,
    private location: Location,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.getVacancy();
  }

  getVacancy(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.service.getVacancy(id)
      .subscribe(vacancy => this.vacancy = vacancy);
  }

  goBack(): void {
    this.location.back();
  }

  deleteVacancy() {
    this.service.deleteVacancy(this.vacancy.id).subscribe(res => {
      this.goBack();
    }, error => {
      console.error(error);
    });
  }

  setFormVacancy() {
    this.formVacancy = this.formBuilder.group({
      id: [this.vacancy.id],
      name: [this.vacancy.name, Validators.required],
      description: [this.vacancy.description],
      salary: [this.vacancy.salary, Validators.required],
      company_id: [this.vacancy.company.id]
    });
  }

  get name() { return this.formVacancy.get('name'); }

  get salary() { return this.formVacancy.get('salary'); }

  saveVacancy() {
    this.service.updateVacancy(this.formVacancy.getRawValue()).subscribe(res => {
      this.getVacancy();
      this.showFormVacancy();
    });
  }

  showFormVacancy() {
    if (this.formUpdateShow) {
      this.formUpdateShow = false;
    } else {
      this.setFormVacancy();
      this.formUpdateShow = true;
    }
  }

  closeFormVacancy() {
    this.showFormVacancy();
  }
}
