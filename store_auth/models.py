from django.db import models

# Create your models here.
class UserRegister(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name
