import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompanyComponent } from './company/company.component';
import { HomeComponent } from './home/home.component';
import { VacancyComponent } from './vacancy/vacancy.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { VacancyDetailComponent } from './vacancy-detail/vacancy-detail.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { TopVacanciesComponent } from './top-vacancies/top-vacancies.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthInterceptor } from './auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    CompanyComponent,
    HomeComponent,
    VacancyComponent,
    VacancyDetailComponent,
    CompanyDetailComponent,
    TopVacanciesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
