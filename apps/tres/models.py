from __future__ import unicode_literals
from django.db import models
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Place(models.Model):
	destination = models.CharField(max_length=255)
	description = models.TextField()
	travel_start = models.CharField(max_length=255)
	travel_end = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	joiner = models.ManyToManyField(User, related_name = "joined_places")
	creator = models.ForeignKey(User, related_name = "created_places")
