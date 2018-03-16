# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import timezone
from django.db import models

# Create your models here.
class UserInfo(models.Model):
	user= models.CharField(max_length = 30)
	pwd = models.CharField(max_length = 30)

# class Publisher(models.Model):
# 	name = models.CharField(max_length=30)
# 	address = models.CharField(max_length=50)
# 	website = models.URLField()

# class Author(models.Model):
# 	email = models.EmailField()
# 	first_name = models.CharField(max_length = 30)
# 	last_name = models.CharField(max_length = 30)

# class Book(models.Model):
# 	title = models.CharField(max_length = 150)
# 	authors = models.ManyToManyField(Author)
# 	publisher = models.ForeignKey(Publisher)

class DoubanMovie(models.Model):
	name = models.CharField(max_length = 200)
	info = models.CharField(max_length = 10000)
	rating = models.CharField(max_length = 20)
	num = models.CharField(max_length = 50)
	quote = models.CharField(max_length = 150)
	img_url = models.CharField(max_length = 300)

