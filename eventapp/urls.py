from django.conf.urls import url
from eventapp import views
from eventapp.Registration.student_registration import register_student
from eventapp.Registration.student_registration import does_student_exists
from eventapp.Registration.society_registration import register_society
from eventapp.events import event_manager
from eventapp.events.event_registration import EventRegistation


urlpatterns = [
     url(r'user$', views.get_user, name='get_user'),
     url(r'exchange_token$', views.get_access_token, name='exchange_token'),
     url(r'register$', register_student, name='register_student'),
     url(r'events$', event_manager.EventView.as_view()),
     url(r'event_signup$', EventRegistation.as_view()),
     url(r'register_society$', register_society, name='register_society'),
     url(r'student_exist$',does_student_exists, name='does_student_exists'),

   
   
   
]