from .models import Client, Tariffs
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'fio', 'telephone', 'data']

class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = ['id', 'name', 'price']