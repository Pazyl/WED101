import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Company, Vacancy
from ..serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2


@csrf_exempt
def all_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()                       # companies - это QuerySet
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})


@csrf_exempt
def one_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company does not exists'})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)

        serializer = CompanySerializer(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'Deleted': True})


@csrf_exempt
def all_vacancies_by_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company does not exists []'})

    vacancies = company.vacancy_set.all()

    if vacancies.__len__() == 0:
        return JsonResponse({'info': 'qazir bul [company] boyinsha  [vacancies] JO-O-O-Q'})
    else:
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def all_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = VacancySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})


@csrf_exempt
def one_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': 'vacancy does not exists'})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)

        serializer = VacancySerializer(instance=vacancy, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'Deleted': True})


@csrf_exempt
def top_ten_vacancies(request):
    if request.method == 'GET':
        top_vacancies = Vacancy.objects.order_by('-salary')[0:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)