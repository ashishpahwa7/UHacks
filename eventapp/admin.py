from django.contrib import admin
from .models import Student,College, Event,Participant, FacultyAdmin, Society


# Register your models here.

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Society)
admin.site.register(FacultyAdmin)