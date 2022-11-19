from rest_framework import serializers
from .models import SuperType


class SuperTypeSerializer(serializers.ModelSerializer):
    model = SuperType
    fields = ['id','type']
    depth = 1