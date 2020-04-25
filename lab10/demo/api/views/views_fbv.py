
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2
from ..models import Company, Vacancy


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()                       # [ companies - это QuerySet ]
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def one_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'Deleted': True})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_vacancies_by_company(request, company_id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': 'company does not exists []'})

        vacancies = company.vacancy_set.all()

        if vacancies.__len__() == 0:
            return Response({'info': 'qazir bul [company] boyinsha  [vacancies] JO-O-O-Q'})
        else:
            serializer = VacancySerializer2(vacancies, many=True)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VacancySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def one_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': 'vacancy does not exists'})

    if request.method == 'GET':
        serializer = VacancySerializer2(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer2(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'Deleted': True})


@api_view(['GET'])
def top_ten_vacancies(request):
    if request.method == 'GET':
        top_vacancies = Vacancy.objects.order_by('-salary')[0:10]
        serializer = VacancySerializer2(top_vacancies, many=True)
        return Response(serializer.data)
