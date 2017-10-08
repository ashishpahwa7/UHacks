from eventapp.models import Student,College
from oauth2_provider.models import AccessToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from oauth2_provider.decorators import protected_resource


@protected_resource()
@api_view(['GET', 'POST', ])
def register_student(request):
	''' Assumes new user has already signed up using Social Auth'''

	try:
		token = request.META.get('HTTP_AUTHORIZATION') # read header information
		token_val = token.split(' ')[1] # read token value
		
		token_obj = AccessToken.objects.get(token=token_val) 

		user = token_obj.user

		college = College.objects.get(name = request.POST['college'])
		course_dict = {'BCA': 0 ,'MCA': 1 }
		course_choices = Student.course_choices

		if Student.objects.filter(user=user).count() ==0 :
			student_instance = Student(user=user,college=college,
				st_name= user.first_name + ' ' + user.last_name, enroll_no = request.POST['enroll_number'],
				course = course_choices[course_dict[request.POST['course']]][0], 
				email = request.POST['email'], contact_number = request.POST['contact'])
		
			student_instance.save()
		
			return Response({"meta": {'status': "0", 'message': 'success'}})

		else:
			return Response({"meta": {'status': "1", 'message': 'You are already registered'}})


	except Exception as e:
		return Response({"meta": {"message":str(e),"status":"2"}})


