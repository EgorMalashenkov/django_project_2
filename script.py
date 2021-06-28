from data import jobs, companies, specialties
from vacancies.models import *
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

if __name__ == "__main__":
    for specialty in specialties:
        Specialty.objects.create(**specialty)

# if __name__ == "__main__":
#     for job in jobs:
#         Vacancy.objects.create(
#             title=job['title'],
#             skills=job['skills'],
#             description=job['description'],
#             salary_min=job['salary_from'],
#             salary_max=job['salary_to'],
#             published_at=job['posted'],
#             specialty=Specialty.objects.get(code=job['specialty']),
#             company=Company.objects.get(id=job['company']),
#
#             )