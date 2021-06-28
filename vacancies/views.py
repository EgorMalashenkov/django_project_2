from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView

from .forms import *
from vacancies.models import *


def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialty': Specialty.objects.all(),
        'companies': Company.objects.all()
        })


def search_view(request):
    specialty_filter = Specialty.objects.filter(code__icontains=request.GET.get('main_search'))
    vacancy_filter_id = specialty_filter[0].id
    return render(request, 'vacancies/search.html', context={
        'vacancies': Vacancy.objects.filter(specialty_id=vacancy_filter_id),
        })


def vacancies_view(request):

    return render(request, 'vacancies/vacancies.html', context={
        "vacancies": Vacancy.objects.all()
    })


def cat_vacancies_view(request, spec_id):

    return render(request, 'vacancies/category.html', context={
        "filtered_category": Vacancy.objects.filter(specialty_id=spec_id)

    })


def company_view(request, company_id):

    return render(request, 'vacancies/company.html', context={
        "company_from_id": Company.objects.filter(id=company_id).first().name,
        "company_vacancies": Vacancy.objects.filter(company__id=company_id),
        "company": Company.objects.get(id=company_id),
    })

#
# @login_required
# def vacancy_view(request, vacancy_id):
#     return render(request, 'vacancies/vacancy.html', context={
#         "vacancy": Vacancy.objects.filter(id=vacancy_id).first(),
#     })


class VacancyView(FormMixin, DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    pk_url_kwarg = 'vacancy_id'
    context_object_name = 'vacancy'
    form_class = CreateApplication
    success_url = '/vacancies/sent'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.vacancy_id = self.kwargs.get('vacancy_id')
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


def send_vacancy(request):
    return render(request, 'vacancies/sent.html')


class CreateCompany(CreateView):
    template_name = 'vacancies/company-edit.html'
    success_url = reverse_lazy('main')
    form_class = CreateCompanyform


def create_company(request):
    pass


def created_company(request):
    return render(request, 'vacancies/index.html')


def my_vacancies(request):
    user_id = request.user.id
    return render(request, 'vacancies/vacancies_list.html', context={
        'vacancies': Vacancy.objects.filter(company_id=user_id),
        'company': Vacancy.objects.get(company_id=user_id),
    })


class VacancyEdit(UpdateView):
    model = Vacancy
    form_class = EditVacancy
    template_name = 'vacancies/vacancy-edit.html'
    pk_url_kwarg = 'vacancy_id'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Applications'] = Application.objects.filter(vacancy_id=self.kwargs['vacancy_id'])
        context['company'] = Vacancy.objects.get(company_id=self.request.user.id)
        return context
