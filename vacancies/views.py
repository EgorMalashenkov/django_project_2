from django.shortcuts import render
from django.db import models
from vacancies.models import Specialty, Company, Vacancy


def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialty': Specialty.objects.all(),
        'company': Company.objects.all()
    })


def vacancies_view(request):

    return render(request, 'vacancies/vacancies.html', context={
        "vacancies": Vacancy.objects.all()
    })


def cat_vacancies_view(request, spec_id):

    return render(request, 'vacancies/category.html', context={
        "filtered_category": Vacancy.objects.filter(specialty__code=spec_id)

    })


def company_view(request, company_id):

    return render(request, 'vacancies/company.html', context={
        "company_from_id": Company.objects.filter(id=company_id).first().name,
        "company_vacancies": Vacancy.objects.filter(company__id=company_id)
    })


def vacancy_view(request, vacancy_id):
    return render(request, 'vacancies/vacancy.html', context={
        "vacancy": Vacancy.objects.filter(id=vacancy_id).first(),
    })

