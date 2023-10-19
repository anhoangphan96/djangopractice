from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=264, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name + " " + self.last_name
