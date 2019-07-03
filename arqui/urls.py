from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.conf import settings
from django.conf.urls.static import static

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')),
    re_path(r'^api/v1/example/', include('example.urls')),
    re_path(r'^api/v1/', include('Alumno.urls')),
    re_path(r'^api/v1/', include('Rfid.urls')),
    re_path(r'^api/v1/asistencia/', include('Asistencia.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
