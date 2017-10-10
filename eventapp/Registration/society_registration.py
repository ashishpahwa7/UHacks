from eventapp.models import Society, College, FacultyAdmin
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from oauth2_provider.decorators import protected_resource
from django.http import JsonResponse



@protected_resource()
@api_view(['GET', 'POST', ])
def register_society(request):
	''' Assumes new user has already signed up using Social Auth'''
	try:
		token = request.META.get('HTTP_AUTHORIZATION') # read header information
		token_val = token.split(' ')[1] # read token value
		
		token_obj = AccessToken.objects.get(token=token_val) 

		user = token_obj.user

		if FacultyAdmin.objects.filter(name=user).exists():
			
			college = College.objects.get(name=request.POST['college_name'])

			society_instance = Society(college=college, society_name = request.POST['society_name'], 
				department= request.POST['department'], facebook_url= request.POST['facebook_url'], 
				website=request.POST['website'])
			society_instance.save()
			return Response({"meta": {'status': "0", 'message': 'success'}})
		else:
			return Response({"meta": {'status': "1", 'message': 'Record Already Exists'}})

	except Exception as e:
		return Response({"meta": {'status': "2", 'error': str(e)}})


