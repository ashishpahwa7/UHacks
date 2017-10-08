from rest_framework import serializers
from eventapp.models import *



class EventSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Event
		fields = ('name' ,'hosted_by','time','venue', 'description','date','img_url','department','id')


class CollegeSerializer(serializers.ModelSerializer):
	
	events = EventSerializer(many=True, read_only=True)
	
	class Meta:
		model = College
		fields = ('college_id','university','img_url', 'name' ,'description','events',)




