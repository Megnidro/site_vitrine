from django.contrib import admin

# Register your models here.

from .models import BekaModel, ClientModel, EquipeModel

admin.site.register(BekaModel)
admin.site.register(ClientModel)
admin.site.register(EquipeModel)