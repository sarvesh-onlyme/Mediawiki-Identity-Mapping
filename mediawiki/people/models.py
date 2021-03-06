from django.db import models
from django.contrib.auth.models import User

class Name(models.Model):
	name = models.CharField(max_length = 30)

class Country(models.Model):
	country = models.CharField(max_length = 30)

class Email(models.Model):
	email = models.EmailField()

class User_email(models.Model):
	user = models.ForeignKey(User)
	email = models.ForeignKey(Email)

class User_name(models.Model):
	user = models.ForeignKey(User)
	name = models.ForeignKey(Name)

class User_country(models.Model):
	user = models.ForeignKey(User)
	country = models.ForeignKey(Country)
