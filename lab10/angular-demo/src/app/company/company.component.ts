import { Component, OnInit } from '@angular/core';
import { Company } from '../Company';
import { ControlDataService } from '../control-data.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[];
  formCompany: FormGroup;
  formCompanyShow = false;

  constructor(private service: ControlDataService, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.getAllCompanies();
    this.setFormCompany();
  }

  getAllCompanies(): void {
    this.service.getAllCompanies()
      .subscribe(companies => this.companies = companies);
  }

  setFormCompany() {
    this.formCompany = this.formBuilder.group({
      name: ['', Validators.required],
      description: [''],
      city: ['', Validators.required],
      address: ['']
    });
  }

  get name() { return this.formCompany.get('name'); }

  get city() { return this.formCompany.get('city'); }

  saveCompany() {
    this.service.createCompany(this.formCompany.getRawValue()).subscribe(res => {
      this.getAllCompanies();
      this.setFormCompany();
    });
  }

  showFormCompany() {
    if (this.formCompanyShow) {
      this.formCompanyShow = false;
      } else {
      this.formCompanyShow = true;
    }
  }

  closeFormCompany() {
    this.setFormCompany();
    this.showFormCompany();
  }
}
