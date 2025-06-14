from django.db import models
from django.utils import timezone
#ID (primary key)

class Contact(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    fone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m', blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.fist_name} {self.last_name}"



