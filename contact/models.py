from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


