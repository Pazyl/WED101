
from django.urls import path
from .views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, AllVacanciesByCompanyAPUView, VacancyListAPIView
from .views.views_cbv import VacancyDetailAPIView, TopVacanciesListAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', AllVacanciesByCompanyAPUView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopVacanciesListAPIView.as_view())
]