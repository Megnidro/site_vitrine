from django.contrib import admin
from .models import Actualite
from ckeditor.widgets import CKEditorWidget
from django import forms


class ActualiteAdminForm(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Actualite
        fields = '__all__'


class ActualiteAdmin(admin.ModelAdmin):
    form = ActualiteAdminForm
    list_display = ('titre', 'date_publication', 'auteur', 'est_publie')
    prepopulated_fields = {'slug': ('titre',)}  # Génère automatiquement le slug à partir du titre
    search_fields = ('titre', 'contenu', 'auteur')
    list_filter = ('date_publication', 'est_publie')
    ordering = ('-date_publication',)
    date_hierarchy = 'date_publication'


admin.site.register(Actualite, ActualiteAdmin)
