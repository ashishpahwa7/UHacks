from django.contrib import admin
from .models import Hospital, Doctor, Disease


# Register your models here.

admin.site.register(Hospital)
admin.site.register(Doctor)
#admin.site.register(Disease)


class DiseaseAdmin(admin.ModelAdmin):
	list_display = ('disease_name','place')



admin.site.register(Disease, DiseaseAdmin)