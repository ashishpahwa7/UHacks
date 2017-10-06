from django.conf.urls import url
from eventapp import views

urlpatterns = [
    url(r'user$', views.get_user, name='get_user'),
     url(r'exchange_token$', views.get_access_token, name='exchange_token'),
   

]