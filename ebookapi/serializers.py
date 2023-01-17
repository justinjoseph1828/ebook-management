from rest_framework import serializers
from .models import ebook


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=ebook
        fields=['id','title','author','genre','review','favorite']