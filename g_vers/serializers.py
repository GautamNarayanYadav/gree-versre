
from .models import *
from rest_framework import serializers


class PhotographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photography
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

