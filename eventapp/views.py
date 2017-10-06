from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.decorators import protected_resource

# Create your views here.

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken


@protected_resource()
def get_user(request):

	''' API view to return user details '''
	try:
		
		token = request.META.get('HTTP_AUTHORIZATION')
		token_val = token.split(' ')[1]
		q = AccessToken.objects.get(token=token_val)
		print("In try block")
	
		return JsonResponse({'user':q.user.username})
	
	except Exception as e:
		return JsonResponse({'status':str(e)})


#TODO : generate convert and refresh token from facebook using user access token
def get_access_token(request):
	pass