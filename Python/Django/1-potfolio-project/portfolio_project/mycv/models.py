from django.db import models


# Create your models here.

class Students(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    birth_date = models.DateField()


class Courses(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)


# model named Post
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    # define a username field with bound max length it can have
    username = models.CharField(max_length=20, blank=False, null=False)
    # This is used to write a post
    text = models.TextField(blank=False, null=False)
    # Values for gender are restricted by giving choices
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    time = models.DateTimeField(auto_now_add=True)
