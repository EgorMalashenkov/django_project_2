from data import jobs, companies, specialties
import django
for companies_data in companies:
    Company.objects.create(**companies_data)


for jobs_data in jobs:
    Vacancy.objects.create(**jobs_data)


for specialties_data in specialties:
    Specialty.objects.create(**specialties_data)
