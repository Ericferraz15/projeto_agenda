from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#ID (primary key)

class category (models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m', blank=True, null=True)
    Category = models.ForeignKey(
        category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
   
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



