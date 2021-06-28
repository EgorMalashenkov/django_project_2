"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import SignupView, MyLoginView
from vacancies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="main"),
    path('search/', search_view, name="search"),
    path('vacancies/', vacancies_view),
    path('vacancies/cat/<int:spec_id>', cat_vacancies_view),
    path('companies/<int:company_id>', company_view),
    path('vacancies/<int:vacancy_id>/', login_required(VacancyView.as_view())),
    path('vacancies/sent', send_vacancy, name='sent'),
    path('mycompany/vacancies', my_vacancies),
    path('mycompany', created_company),
    path('register', SignupView.as_view()),
    path('login', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('mycompany/letscreate', CreateCompany.as_view()),
    path('vacancy/edit/<int:vacancy_id>/', VacancyEdit.as_view(), name="VacancyEdit")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
