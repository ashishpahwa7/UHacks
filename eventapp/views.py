from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.decorators import protected_resource

# Create your views here.

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken

import requests
from django.conf import settings
import json

from .models import Doctor, Hospital, Disease
from .serializers import DoctorSerializer, DiseaseSerializer, Disease1Serializer



def get_hospital(username,password):
	
	doc_name = Doctor.objects.get(username=username, password=password)

	d_name = doc_name.name
	h_add = doc_name.hospital

	return d_name,h_add



def validate_request(username, password):
	if Doctor.objects.filter(username=username, password=password).exists():
		return True
	else:
		return False


@api_view(['GET', 'POST', ])
def register_disease(request):

	username = request.POST['username']
	password = request.POST['password']
	disease_name = request.POST['dis']
	lat = request.POST['lat']
	lon = request.POST['lon']

	if validate_request(username, password):
		doc_name = Doctor.objects.get(username=username,password=password)
		
		d_name, h_name = get_hospital(username, password)

		dis_instande = Disease(doc_name=doc_name, h_name=h_name, disease_name=disease_name,lon=lon, lat=lat)
		dis_instande.save()
		return JsonResponse({'status': True})



@api_view(['GET', 'POST', ])
def login_usr(request):

	try:
		doc_quer = Doctor.objects.filter(username= request.POST['username'], password=request.POST['password'])
		serializer = DoctorSerializer(doc_quer, many=True, context={'request': request})
		return JsonResponse(serializer.data, safe=False)
	
	except Exception as e:
		return JsonResponse({'error': str(e)})



@api_view(['GET', 'POST', ])
def get_geo_data(request):
		try:
			disease_name = request.POST['disease']
			if disease_name:
				data = Disease.objects.filter(disease_name= disease_name)
				serializer = DiseaseSerializer(data, many=True, context={'request': request})
				return JsonResponse(serializer.data, safe=False)
			else:
				data = Disease.objects.all()
				serializer = Disease1Serializer(data, many=True, context={'request': request})
				return JsonResponse(serializer.data, safe=False)

		except Exception as e:
			return JsonResponse({'error':str(e)})




'''

Statistical Analysis




'''