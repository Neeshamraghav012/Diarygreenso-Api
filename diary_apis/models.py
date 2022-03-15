from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime



class Course(models.Model):

	CHOICES = (

		('Videos', 'Videos'),
		('Textual', 'Textual'),
		('Hybrid', 'Hybrid'),
	)

	name = models.CharField(max_length = 1000)
	author = models.CharField(max_length = 1000)
	description = models.CharField(max_length = 5000)
	about = models.TextField(null = True, blank = True)
	link = models.URLField(max_length = 2000)
	overall_rating = models.IntegerField(default = 0)
	price = models.IntegerField(default = 0)
	catagory = models.CharField(max_length = 250, default="Computer Science")
	platform = models.CharField(max_length = 1000, default="YouTube")
	released_date = models.DateField(null = True, blank = True)
	country = models.CharField(max_length = 1000, default="India")
	language = models.CharField(max_length = 250, default="English")
	price = models.IntegerField(default = 0)
	duration = models.IntegerField(default=4)
	certificate = models.BooleanField(default = False)
	material_type = models.CharField(max_length = 25, choices = CHOICES, default="Videos")
	added_by = models.CharField(max_length = 1000, default="Neesham")


	def __str__(self):

		return f"{self.name}"

	class  Meta:

		verbose_name_plural = "Courses-sinx"
		ordering = ["-overall_rating"]
