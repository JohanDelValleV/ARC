from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

urlpatterns = [
    re_path(r'^', CustonAuthToken.as_view())
]