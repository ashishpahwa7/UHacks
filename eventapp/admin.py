from django.contrib import admin
from .models import Student,College, Event,Participant


# Register your models here.

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Event)
admin.site.register(Participant)