from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    address = models.TextField()

    def __str__(self):
        return self.name