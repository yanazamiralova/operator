from django.contrib import admin
from .models import Client, Tariffs, Areas, Records, Account

admin.site.register(Client)
admin.site.register(Tariffs)
admin.site.register(Areas)
admin.site.register(Records)
admin.site.register(Account)
