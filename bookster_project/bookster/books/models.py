from django.db import models

# Create your models here.

class Subjects(models.Model):
    subject_name = models.CharField(max_length=30)

class Mathsb(models.Model):
    book_name = models.CharField(max_length=30)

class Physicsb(models.Model):
    book_name = models.CharField(max_length=30)

class Englishb(models.Model):
    book_name = models.CharField(max_length=30)

class Bmeb(models.Model):
    book_name = models.CharField(max_length=30)

class Beb(models.Model):
    book_name = models.CharField(max_length=30)

class Bmewb(models.Model):
    book_name = models.CharField(max_length=30)

class Ecwb(models.Model):
    book_name = models.CharField(max_length=30)

class Bewb(models.Model):
    book_name = models.CharField(max_length=30)
