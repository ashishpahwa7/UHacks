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



def get_sub_locality(latitude,longitude):


    sensor = 'true'

    base = "http://maps.googleapis.com/maps/api/geocode/json?"

    params = "latlng={lat},{lon}&sensor={sen}".format(lat=latitude,lon=longitude,sen=sensor)
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url).json()
    print(response['results'][0]['address_components'])

    for  item in response['results'][0]['address_components']:
        for categ in item['types']:
            if 'sublocality' or 'sublocality_level_2' or 'sublocality_level_3' in categ:
                print(item['short_name'])
                return item['short_name']  



@api_view(['GET', 'POST', ])
def get_total_patient(request):

	try:
		patient_count = Disease.objects.filter(disease_name=request.POST['disease']).count()
		return JsonResponse({'count': patient_count})
	except Exception as e:
		return JsonResponse({'error': str(e)})


@api_view(['GET', 'POST', ])
def get_disease_distribution(request):

	q = Disease.objects.filter(disease_name=request.POST['disease_name'].lower()).values('place').annotate(total=Count('place'))

	data = []
	for patient in q:
		print(patient['place'])
		temp = Disease.objects.filter(place=patient['place'])[0]
		#print(temp.lat, temp.lon)
		#print(patient)
		data.append(
			{'center' : { 'lat':float(temp.lat) ,  'lng': float(temp.lon) },'population': patient['total']*69, 'place': patient['place']
			 
			  }
			)
		print(data)

	return JsonResponse(data,safe=False)
	#return JsonResponse([{'population': 100000, 'center': {'lat': 28.688, 'lng': 77.176}, 'place': 'ashok vihar'}, {'population': 50000, 'center': {'lat': 28.525, 'lng': 77.207}, 'place': 'saket'}],safe=False)


@api_view(['GET', 'POST', ])
def date_filter(request):

	try:
		from_date = request.POST['from_date']
		to_date = request.POST['to_date']

		dis_dic = {}
		q = Disease.objects.filter(date_time__range=[from_date, to_date]).values('disease_name').annotate(total=Count('disease_name'))
		for item in q:
			dis_dic[item['disease_name']] = item['total']
		return JsonResponse(dis_dic)
	except Exception as e:
		return JsonResponse({'error': str(e)})


@api_view(['GET', 'POST', ])
def date_filter_by_locality(request):

	try:
		from_date = request.POST['from_date']
		to_date = request.POST['to_date']
		place = request.POST['place']

		dis_dic = {}
		q = Disease.objects.filter(date_time__range=[from_date, to_date], place=place).values('disease_name').annotate(total=Count('disease_name'))
		for item in q:
			dis_dic[item['disease_name']] = item['total']
		return JsonResponse(dis_dic)
	except Exception as e:
		return JsonResponse({'error': str(e)})



@api_view(['GET', 'POST', ])
def date_filter_by_disease(request):

	try:
		from_date = request.POST['from_date']
		to_date = request.POST['to_date']
		disease_name = request.POST['disease_name']

		dis_dic = {}
		q = Disease.objects.filter(date_time__range=[from_date, to_date], disease_name=disease_name).values('place').annotate(total=Count('place'))
		for item in q:
			dis_dic[item['place']] = item['total']
		return JsonResponse(dis_dic)
	except Exception as e:
		return JsonResponse({'error': str(e)})


@api_view(['GET', 'POST', ])
def time_series_plot(request):
	
	from_date = request.POST['from_date']
	to_date = request.POST['to_date']
	disease_name = request.POST['disease_name']

	X = []
	Y = []

	q = Disease.objects.filter(date_time__range=[from_date, to_date], disease_name=disease_name).values('date_time').annotate(total=Count('date_time'))
	for item in q:
		X.append(item['date_time'].strftime('%d-%m-%Y'))
		Y.append(item['total'])

	return JsonResponse({'X':str(X), 'Y':str(Y)})
	


@api_view(['GET', 'POST', ])
def time_series_plot_by_locality(request):
	
	from_date = request.POST['from_date']
	to_date = request.POST['to_date']
	disease_name = request.POST['disease_name']
	place = request.POST['place']

	X = []
	Y = []

	q = Disease.objects.filter(date_time__range=[from_date, to_date], disease_name=disease_name, place=place).values('date_time').annotate(total=Count('date_time'))
	for item in q:
		X.append(item['date_time'].strftime('%d-%m-%Y'))
		Y.append(item['total'])

	return JsonResponse({'X':str(X), 'Y':str(Y)})


@api_view(['GET', 'POST', ])
def quant_analysis(request):
	place = request.POST['place']
	
	result = {}

	#total_patient_count = Disease.objects.filter(place=place).count()

	diseses = Disease.objects.values('disease_name').distinct()
	print(diseses)

	#total_patients = Disease.objects.filter().count()
	#q_local = Disease.objects.filter(place=place).values('disease_name').annotate(total=Count('disease_name'))


	for item in diseses:
		q_net = Disease.objects.filter(disease_name=item['disease_name']).values('disease_name').annotate(total=Count('disease_name'))
		place_dis_count = Disease.objects.filter(disease_name=item['disease_name'], place=place).values('disease_name').annotate(total=Count('disease_name'))
		#print(item['disease_name'])
		#print(q_net)
		print(place_dis_count)
		#print(place_dis_count[0]['total']/q_net[0]['total'])
		result[item['disease_name']] = (place_dis_count[0]['total']/q_net[0]['total'])*100

	return JsonResponse({'data':result})



@api_view(['GET', 'POST', ])
def locality_analysis(request):
	place = request.POST['place']
	
	data = []

	total_patient_count = Disease.objects.filter(place=place).count()

	diseses = Disease.objects.values('disease_name').distinct()
	q_local = Disease.objects.filter(place=place).values('disease_name').annotate(total=Count('disease_name'))
	print(total_patient_count)
	
	for item in q_local:
		data.append({ item['disease_name'] : (item['total']/total_patient_count)*100 })

	return JsonResponse({'data':data})


@api_view(['GET', 'POST', ])
def locality__analysis_2(request):
	place = request.POST['place']
	from_date = request.POST['from_date']
	to_date = request.POST['to_date']
	
	data = []

	total_patient_count = Disease.objects.filter(date_time__range=[from_date, to_date], place=place).count()

	diseses = Disease.objects.values('disease_name').distinct()
	q_local = Disease.objects.filter(date_time__range=[from_date, to_date], place=place).values('disease_name').annotate(total=Count('disease_name'))
	print(total_patient_count)
	
	for item in q_local:
		data.append({ item['disease_name'] : (item['total']/total_patient_count)*100 })

	return JsonResponse({'data':data})