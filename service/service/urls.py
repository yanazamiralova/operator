from django.contrib import admin
from django.urls import path
from myapp.views import ClientList, ClientDetail, TariffsList, TariffsDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', ClientList.as_view(), name='client-list'),
    path('client/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('tariffs/',  TariffsList.as_view(), name='tariffs-list'),
    path('tariffs/<int:pk>/', TariffsDetail.as_view(), name='tariffs-detail'),
]
