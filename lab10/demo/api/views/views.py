from django.shortcuts import render

from django.http.response import JsonResponse

from ..models import Company, Vacancy


def all_companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def one_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company does not exists'})

    return JsonResponse(company.to_json())


def all_vacancies_by_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company does not exists []'})

    vacancies = company.vacancy_set.all()

    if vacancies.__len__() == 0:
        return JsonResponse({'info': 'qazir bul [company] boyinsha  [vacancies] JO-O-O-Q'})
    else:
        json_vacancies = [v.to_json() for v in vacancies]
        return JsonResponse(json_vacancies, safe=False)


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(json_vacancies, safe=False)


def one_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': 'vacancy does not exists'})

    return JsonResponse(vacancy.to_json())


def top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[0:10]
    json_top_vacancies = [v.to_json() for v in top_vacancies]
    return JsonResponse(json_top_vacancies, safe=False)