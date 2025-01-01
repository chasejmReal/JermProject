#Test/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


#CLASS: CustomUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add more custom fields if needed
    # For example, a phone number:
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
