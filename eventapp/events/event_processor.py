from eventapp.models import Event,College
from eventapp.serializers import CollegeSerializer
from rest_framework import viewsets, generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from oauth2_provider.decorators import protected_resource


class EventView(View):
	

	def get(self, request):
		queryset = College.objects.all()
		serializer = CollegeSerializer(queryset, many=True, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

	def post(self,request):
		return JsonResponse({'message':'success'})

	@method_decorator(csrf_exempt)
	@method_decorator(protected_resource())
	def dispatch(self, request, *args, **kwargs):
		return super(EventView, self).dispatch(request, *args, **kwargs)

