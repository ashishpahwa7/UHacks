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

from .models import Doctor, Hospital





def register_disease(requests):
	pass


@api_view(['GET', 'POST', ])
def authenticate(username, password):

	if Doctor.objects.filter(username=username, password=password).exists():
		return True
	else:
		return False



