from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    cateogry = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
