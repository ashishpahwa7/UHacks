from django.db import models
from datetime import datetime    




class Hospital(models.Model):

	name = models.CharField(max_length=100, primary_key=True)
	address = models.CharField(max_length=100)
	sector_choices = (('a','Private'),('b','Government'),('c','Semi-Private'),('d','Other'))
	sector = models.CharField(max_length=1, choices=sector_choices)

	class Meta:
		unique_together = (("name","address"),)


	def __str__(self):
		return self.name



class Doctor(models.Model):

	username = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)
	hospital = models.ForeignKey('Hospital')
	license_number = models.CharField(max_length=100)

	class Meta:
		unique_together = (('username','license_number'))

	def __str__(self):
		return self.name

class disease(models.Model)
	
	doc_name = models.ForeignKey('Doctor')
	h_name = models.ForeignKey('Hospital')
	disease_name = models.CharField(max_length=20)
	lon = models.DecimalField(max_digits=8, decimal_places=3)
	lat = models.DecimalField(max_digits=8, decimal_places=3)

	def __str__(self):
		return self.disease_name
