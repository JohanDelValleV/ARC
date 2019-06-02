from rest_framework import routers, serializers, viewsets

from example.models import Example

class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('__all__')
        