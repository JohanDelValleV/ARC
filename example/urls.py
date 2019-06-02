from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from example import views

urlpatterns = [
    re_path(r'example_lista/$', views.ExampleList.as_view()),
]