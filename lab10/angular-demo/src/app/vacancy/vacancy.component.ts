import { Component, OnInit } from '@angular/core';
import { Company } from '../Company';
import { Vacancy } from '../Vacancy';
import { ControlDataService } from '../control-data.service';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {
  companyVacancies: Vacancy[];
  company: Company;
  formVacancy: FormGroup;
  formVacancyShow = -1;

  constructor(
    private service: ControlDataService,
    private route: ActivatedRoute,
    private formBuilder2: FormBuilder
  ) { }

  ngOnInit(): void {
    this.getCompany();
    this.getAllVacanciesByCompany();
  }

  getAllVacanciesByCompany(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.service.getAllVacanciesByCompany(id)
      .subscribe(companyVacancies => this.companyVacancies = companyVacancies);
  }

  getCompany(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.service.getCompany(id)
      .subscribe(company => this.company = company);
  }

  setFormVacancy() {
    this.formVacancy = this.formBuilder2.group({
      name: ['', Validators.required],
      description: [''],
      salary: [, Validators.required],
      company_id: [this.company.id]
    });
  }

  get name() { return this.formVacancy.get('name'); }

  get salary() { return this.formVacancy.get('salary'); }

  saveVacancy() {
    this.service.createVacancy(this.formVacancy.getRawValue(), this.company.id).subscribe(res => {
      this.getAllVacanciesByCompany();
      this.setFormVacancy();
    });
  }

  showFormVacancy() {
    if (this.formVacancyShow === -1) {
      this.setFormVacancy();
      this.formVacancyShow = 1;
    } else if (this.formVacancyShow === 1){
      this.formVacancyShow = 2;
    } else {
      this.formVacancyShow = 1;
    }
  }

  closeFormVacancy() {
    this.setFormVacancy();
    this.showFormVacancy();
  }
}
