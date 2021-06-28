from django.contrib import admin
from django.contrib.auth.models import User
if __name__ == "__main__":
    User.objects.create_user(
        username='usual_user', email='user@example.com', password='NotSecRetAtAll'
    )
# Register your models here.
