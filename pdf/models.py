from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    about = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    publications = models.TextField(max_length=1000)
    awards = models.TextField(max_length=1000)
    certifications = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    