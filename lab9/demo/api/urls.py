from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.all_companies),
    path('companies/<int:company_id>/', views.one_company),
    path('companies/<int:company_id>/vacancies/', views.all_vacancies_by_company),
    path('vacancies/', views.all_vacancies),
    path('vacancies/<int:vacancy_id>/', views.one_vacancy),
    path('vacancies/top_ten/', views.top_ten_vacancies),
]