from django.contrib import admin
from .models import OffreEmploi


class OffreEmploiAdmin(admin.ModelAdmin):
    list_display = (
        'numero_offre', 'titre', 'type_contrat', 'lieu', 'date_publication', 'est_active', )
    list_filter = ('type_contrat', 'est_active', 'date_publication')
    search_fields = ('titre', 'description', )
    prepopulated_fields = {"slug": ("titre",)}
    ordering = ['-date_publication']


admin.site.register(OffreEmploi, OffreEmploiAdmin)
