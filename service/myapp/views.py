from django.shortcuts import render
from rest_framework import generics
from .models import Client, Tariffs, Areas, Records, Account
from .serializers import ClientSerializer, TariffsSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = Client

class TariffsList(generics.ListCreateAPIView):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer

class TariffsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tariffs.objects.all()
    serializer_class = Tariffs

# class AreasList(generics.ListCreateAPIView):
#     queryset = Areas.objects.all()
#     serializer_class = AreasSerializer

# class AreasDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Areas.objects.all()
#     serializer_class = Areas

# class RecordsList(generics.ListCreateAPIView):
#     queryset = Records.objects.all()
#     serializer_class = RecordsSerializer

# class RecordsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Records.objects.all()
#     serializer_class = Records

# class AccountList(generics.ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = Account
