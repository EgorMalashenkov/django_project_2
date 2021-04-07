from django.shortcuts import render
from vacancies.models import Company


def main_view(request):
    return render(request, 'vacancies/index.html')


def vacancies_view(request):

    return render(request, 'vacancies/vacancies.html')


def spec_vacancies_view(request, person_id):
    return render(request, 'vacancies/index.html')


def company_view(request, company_id):
    return render(request, 'vacancies/company.html')


def vacancy_view(request, vacancy_id):
    return render(request, 'vacancies/vacancy.html')
