from django.conf.urls import url
from eventapp import views


urlpatterns = [
     #url(r'user$', views.get_user, name='get_user'),
     #url(r'exchange_token$', views.get_access_token, name='exchange_token'),
     url(r'register_disease$', views.register_disease, name='register_disease'),
     url(r'login$', views.login_usr, name='login'),
     url(r'geo_data$', views.get_geo_data, name='geo_data'),
     #url(r'register_society$', register_society, name='register_society'),
     #url(r'student_exist$',does_student_exists, name='does_student_exists'),  
]