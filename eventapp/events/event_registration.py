from eventapp.models import Event, Student, Participant
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from oauth2_provider.decorators import protected_resource
from rest_framework.response import Response
from oauth2_provider.models import AccessToken
from django.http import JsonResponse
from rest_framework.response import Response



class EventRegistation(View):

	def post(self, request):

		token = request.META.get('HTTP_AUTHORIZATION')
		token_val = token.split(' ')[1]

		student = self.does_student_exists(token_val)
		event = self.get_event_record(request.POST['event_id'])
		print(student,event)

		if student != 'error' and event !='error':
			if Participant.objects.filter(name=student,event=event).exists():
				return JsonResponse({"meta": {'status': "1", 'message': 'You have already registered for this event'}})
			try:
				participant_instance = Participant(name=student,event=event)
				participant_instance.save()
				return JsonResponse({"meta": {'status': "0", 'message': 'success'}})
			except Exception as e:
				return JsonResponse({"meta": {'status': "2", 'error': str(e)}})
		else:
			return JsonResponse({"meta": {'status': "1", 'message': 'Something went wrong'}})



	def does_student_exists(self, token):
		try:
			#first  check whether the user exists or not
			token_obj = AccessToken.objects.get(token=token)
			# if user exists test if user is registered as a student
			if token_obj:
				student_obj = Student.objects.get(user=token_obj.user)
				return student_obj
			else:
				return 'error'
		except Exception as e:
			return str(e)


	def get_event_record(self, event_id):
		try:
			event = Event.objects.get(id=event_id)
			return event
		except:
			return 'error'

	@method_decorator(csrf_exempt)
	@method_decorator(protected_resource())
	def dispatch(self, request, *args, **kwargs):
		return super(EventRegistation, self).dispatch(request, *args, **kwargs)







		
