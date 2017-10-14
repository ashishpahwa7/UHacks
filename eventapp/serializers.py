from rest_framework import serializers
from eventapp.models import *




class DoctorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Doctor
		fields = ('name' ,'specialization','hospital','license_number')



class DiseaseSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Disease
		fields = ('lat' ,'lon')



class Disease1Serializer(serializers.ModelSerializer):
	
	class Meta:
		model = Disease
		fields = ('lat' ,'lon','disease_name')