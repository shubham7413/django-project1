from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10,null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return  (self.email)