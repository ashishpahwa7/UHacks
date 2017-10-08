from eventapp.models import Event,College
from eventapp.serializers import CollegeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from oauth2_provider.decorators import protected_resource

#TODO : Allow only admin students or faculty to create or delete event and record the action in event_logs

class EventView(View):
	
	def get(self, request):
		queryset = College.objects.all()
		serializer = CollegeSerializer(queryset, many=True, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

	def post(self,request):
		try:
			college = College.objects.get(name=request.POST['college_name'])
			event_insatnce = Event(name=request.POST['event_name'], date=request.POST['event_date'],
				venue=request.POST['event_venue'], time=request.POST['event_time'], 
				description= request.POST['event_desc'], hosted_by= request.POST['event_host'], 
				img_url= request.POST['img_url'], department = request.POST['department'],college=college)
			event_insatnce.save()

			return JsonResponse({"meta": {'status': "0", 'message': 'success'}})

		except Exception as e:
			return JsonResponse({"meta": {'status': "2", 'error': str(e)}})


	@method_decorator(csrf_exempt)
	#@method_decorator(protected_resource())
	def dispatch(self, request, *args, **kwargs):
		return super(EventView, self).dispatch(request, *args, **kwargs)

