from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('RESIDENT','Resident'),
        ('COMPANY','Company'),
        ('ADMIN','Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='RESIDENT')
    phone = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

