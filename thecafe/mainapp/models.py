from django.db import models

# Create your models here.


class carousel(models.Model):
    number = models.CharField(max_length=3, blank=True)
    state = models.CharField(max_length=10, blank=True)
    image = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=25)
    sdesc = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class Information(models.Model):
    about = models.TextField()
    phone = models.CharField(max_length=10)
    link = models.CharField(max_length=500)
