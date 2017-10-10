from django.db import models
from datetime import datetime    

class College(models.Model):

	college_id = models.CharField(max_length=10,primary_key=True)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	university = models.CharField(max_length=200,null=True,blank=True)
	img_url = models.CharField(max_length=300,blank=True,null=True)


	def __str__(self):
		return self.name


class Society(models.Model):
	college = models.ForeignKey('College')
	society_name = models.CharField(max_length=50)
	department = models.CharField(max_length=20, default='Technical')
	facebook_url = models.CharField(max_length=100, default=None)
	website = models.CharField(max_length=20,null=True, blank=True)


	class Meta:
		unique_together = (("college", "society_name"),)


	def __str__(self):
		return self.s_name



class Student(models.Model):
	
	user = models.ForeignKey('auth.User',default=None)
	college = models.ForeignKey('college')
	st_name = models.CharField(max_length=50)
	enroll_no = models.BigIntegerField(primary_key=True)
	st_society = models.ForeignKey('society',blank=True,null=True)
	course_choices = (('a','BCA'),('b','MCA'),('c','BA LLB'),('d','BBA LLB'),('e','LL.M'),('f','Eco. Hons.'),('g','BA(JMC)'),('h','BBA'),('i','BBA(B&I)'),('j','B.Com(H)'))
	course = models.CharField(max_length=1, choices=course_choices)
	email = models.EmailField(unique=True)
	contact_number = models.BigIntegerField()


	def __str__(self):
		return self.st_name


class StudentAdmin(models.Model):
	name = models.ForeignKey('auth.user')
	enroll_no = models.ForeignKey('student')
	email = models.EmailField(unique=True)
	contact_number = models.BigIntegerField()


	def __str__(self):
		return self.name


class FacultyAdmin(models.Model):
	name = models.ForeignKey('auth.user')
	email = models.EmailField(unique=True)
	contact_number = models.BigIntegerField()

	def __str__(self):
		return self.name


class Event(models.Model):
	
	name = models.CharField(max_length=100)
	date = models.CharField(max_length=20)
	venue = models.CharField(max_length=200)
	time = models.CharField(max_length=50)
	description = models.TextField()
	college = models.ForeignKey('College',related_name = 'events')
	hosted_by = models.CharField(max_length=100)
	img_url = models.CharField(max_length=300,blank=True,null=True)
	department = models.CharField(max_length=100,null=True,blank=True)


	def __str__(self):
		return self.name



class Participant(models.Model):
	
	name = models.ForeignKey('Student')
	event = models.ForeignKey('Event')
	reg_date = models.DateTimeField(default=datetime.now)

	class Meta:
		unique_together = (("name", "event"),)


	def __str__(self):
		return self.name.user.username

