from django.contrib import admin
from .models import ServicesModel, ProjetModel


# Register your models here.


class ServicesModelAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'is_home')  # Ce que vous voulez afficher dans la vue liste
    search_fields = ('title', 'content')  # Champs de recherche
    prepopulated_fields = {'slug': ('title',)}  # Pour auto-générer le slug à partir du titre
    list_per_page = 50


#admin.site.register(ServicesModel, ServicesModelAdmin)
admin.site.register(ProjetModel)