from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Rfid import views
 
urlpatterns = [
    re_path(r'rfid/$', views.RfidList.as_view()),
    re_path(r'rfid/(?P<id>\d+)$', views.RfidDetail.as_view()),
]