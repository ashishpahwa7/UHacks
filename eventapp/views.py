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



@protected_resource()
def get_user(request):
	''' API view to return user details '''
	try:
		
		token = request.META.get('HTTP_AUTHORIZATION')
		token_val = token.split(' ')[1]
		q = AccessToken.objects.get(token=token_val)
	
		return JsonResponse({'user':q.user.username})
	
	except Exception as e:
		return JsonResponse({'status':str(e)})


@csrf_exempt
def get_access_token(request):

	API_ENDPOINT = "https://vips-events.herokuapp.com/auth/convert-token"
	try:
		data = {'grant_type':'convert_token', 'client_id':settings.CLIENT_ID, 'backend':'facebook', 'token':request.POST['user_access_token'], 'client_secret': settings.CLIENT_SECRET }
		r = requests.post(url = API_ENDPOINT, data = data)
		data = r.json()
		return JsonResponse(data)
	except Exception as e:
		return JsonResponse({'error':str(e)})