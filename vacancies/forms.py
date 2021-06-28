from django import forms
from vacancies.models import Company, Application, Vacancy


class CreateCompanyform(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class CreateApplication(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'phone', 'cover_letter')
        labels = {'name': 'Ваше имя',
                  'phone': 'Телефон',
                  'cover_letter': 'Сопроводительное письмо'}


class EditVacancy(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'skills', 'description', 'salary_min', 'salary_max')
        labels = {
                  'title': 'Название',
                  'skills': 'Требования',
                  'description': 'Описание',
                  'salary_min': 'Зарплата от',
                  'salary_max': 'Зарплата до',
                  }
