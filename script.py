from data import jobs, companies, specialties
from vacancies.models import Company, Vacancy, Specialty

if __name__ == "__main__":
    Company.objects.create(
        name="ABC",
        location="spbssss",
        description="asda",
        employee_count=2
                          )