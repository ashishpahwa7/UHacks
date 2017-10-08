from django.db import models

class College(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)


	def __str__(self):
		return self.name


class Society(models.Model):
	college = models.ForeignKey('college')
	s_name = models.CharField(max_length=50)
	field = models.CharField(max_length=20,default='Technical')


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