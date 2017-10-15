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

from django.db.models import Count



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
	disease_name = request.POST['disease_name'].lower()
	lat = request.POST['lat']
	lon = request.POST['lon']
	place = request.POST['place']

	if validate_request(username, password):
		doc_name = Doctor.objects.get(username=username,password=password)
		
		d_name, h_name = get_hospital(username, password)

		dis_instande = Disease(doc_name=doc_name, h_name=h_name, disease_name=disease_name,lon=lon, lat=lat,place=place)
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
def custom_plot(request):
	
		try:
			disease_name = request.POST['disease'].lower()
			place = request.POST['place']
			lat = request.POST['lat']
			lon = request.POST['lng']

			if disease_name and place:
				dis_count = Disease.objects.filter(disease_name= disease_name, place=place).count()
				#return JsonResponse({'population': dis_count})
				return JsonResponse({'center' : { 'lat':float(lat) ,  'lng': float(lon) },'population':dis_count*69, 'place': place})		

		except Exception as e:
			return JsonResponse({'error':str(e)})




@api_view(['GET', 'POST', ])
def plot_by_place(request):
	
		try:
			place_dic = {}
			place = request.POST['place']
			res = Disease.objects.filter(place=place).values('disease_name').annotate(total=Count('disease_name'))
			for item in res:
				place_dic[item['disease_name']] = item['total']
			return JsonResponse(place_dic)

		except Exception as e:
			return JsonResponse({'error':str(e)})


@api_view(['GET', 'POST', ])
def plot_by_disease(request):
	
		try:
			place_dic={}
			disease_name = request.POST['disease_name']
			res = Disease.objects.filter(disease_name=disease_name).values('place').annotate(total=Count('place'))
			for item in res:
				place_dic[item['place']] = item['total']
			return JsonResponse(place_dic)

		except Exception as e:
			return JsonResponse({'error':str(e)})