import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Company } from './Company';
import { Vacancy } from './Vacancy';
import { LoginResponse } from './models';

@Injectable({
  providedIn: 'root'
})
export class ControlDataService {
  private path = 'http://127.0.0.1:8000/api/';

  constructor(private http: HttpClient) { }

  getAllCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(this.path + 'companies/');
  }
  getAllVacanciesByCompany(id: string): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.path + 'companies/' + id + '/vacancies/');
  }
  getCompany(id: string): Observable<Company> {
    return this.http.get<Company>(this.path + 'companies/' + id);
  }


  getAllVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.path + 'vacancies/');
  }
  getTopVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.path + 'vacancies/top_ten/');
  }
  getVacancy(id: string): Observable<Vacancy> {
    return this.http.get<Vacancy>(this.path + 'vacancies/' + id);
  }


  createCompany(company: Company): Observable<Company> {
    return this.http.post<Company>(this.path + 'companies/', company);
  }
  createVacancy(vacancy: Vacancy, id): Observable<Vacancy> {
    return this.http.post<Vacancy>(this.path + 'companies/' + id + '/vacancies/', vacancy);
  }


  updateCompany(company: Company) {
    return this.http.put(this.path + 'companies/' + company.id + '/', company);
  }
  updateVacancy(vacancy: Vacancy) {
    return this.http.put(this.path + 'vacancies/' + vacancy.id + '/', vacancy);
  }


  deleteCompany(id) {
    return this.http.delete(this.path + 'companies/' + id);
  }
  deleteVacancy(idVacancy) {
    return this.http.delete(this.path + 'vacancies/' + idVacancy);
  }


  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(this.path + 'login/', {
      username,
      password
    });
  }
}


// http://127.0.0.1:8000/api/companies/

// http://127.0.0.1:8000/api/companies/1/vacancies/
