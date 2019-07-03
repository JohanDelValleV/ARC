from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Asistencia import views
 
urlpatterns = [
    re_path(r'asistencia', views.AsistenciaCheckout.as_view()),    
    
]