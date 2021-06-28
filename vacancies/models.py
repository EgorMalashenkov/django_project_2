from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR')
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR')


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.published_at = timezone.now()
        return super(Vacancy, self).save(*args, **kwargs)


class Application(models.Model):
    name = models.CharField(max_length=24)
    phone = models.CharField(max_length=12)
    cover_letter = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
