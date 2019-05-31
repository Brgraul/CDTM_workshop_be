from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.http import request


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    desc= models.CharField(max_length=400)
    date_posted = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete="cascade", null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

