from data import jobs, companies, specialties
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "conf.settings"
django.setup()
from vacancies.models import Company, Vacancy, Specialty


if __name__ == "__main__":

    for jobs_data in jobs:
        Vacancy.objects.create(**jobs_data)




#if __name__ == "__main__":
    #Specialty.objects.all().delete()