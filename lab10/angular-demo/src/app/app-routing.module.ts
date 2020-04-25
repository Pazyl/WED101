import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyComponent } from './company/company.component';
import { HomeComponent } from './home/home.component';
import { VacancyComponent } from './vacancy/vacancy.component';
import { VacancyDetailComponent } from './vacancy-detail/vacancy-detail.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { TopVacanciesComponent } from './top-vacancies/top-vacancies.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },

  { path: 'companies', component: CompanyComponent },
  { path: 'companies/:id', component: CompanyDetailComponent },
  { path: 'companies/:id/vacancies', component: VacancyComponent },

  { path: 'vacancies/:id', component: VacancyDetailComponent },
  { path: 'top-vacancies', component: TopVacanciesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
