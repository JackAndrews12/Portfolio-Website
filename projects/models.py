from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=2083)


class Contact(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=100)
