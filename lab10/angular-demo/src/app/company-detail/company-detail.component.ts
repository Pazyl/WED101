import { Component, OnInit } from '@angular/core';
import { Company } from '../Company';
import { ControlDataService } from '../control-data.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  company: Company;
  formCompanyShow = false;
  formCompany: FormGroup;

  constructor(
    private service: ControlDataService,
    private route: ActivatedRoute,
    private location: Location,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.service.getCompany(id)
      .subscribe(company => this.company = company);
  }

  goBack(): void {
    this.location.back();
  }

  deleteCompany(id) {
    this.service.deleteCompany(id).subscribe(res => {
      this.goBack();
    }, error => {
      console.error(error);
    });
  }

  setFormCompany() {
    this.formCompany = this.formBuilder.group({
      id: [this.company.id],
      name: [this.company.name, Validators.required],
      description: [this.company.description],
      city: [this.company.city, Validators.required],
      address: [this.company.description]
    });
  }

  get name() { return this.formCompany.get('name'); }

  get city() { return this.formCompany.get('city'); }

  saveCompany() {
    this.service.updateCompany(this.formCompany.getRawValue()).subscribe(res => {
      this.getCompany();
      this.showFormCompany();
    });
  }

  showFormCompany() {
    if (this.formCompanyShow) {
      this.formCompanyShow = false;
    } else {
      this.setFormCompany();
      this.formCompanyShow = true;
    }
  }

  closeFormCompany() {
    this.showFormCompany();
  }
}
