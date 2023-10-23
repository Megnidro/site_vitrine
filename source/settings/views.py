from django.views.generic import TemplateView

from .models import BekaModel, ClientModel, EquipeModel
from services.models import ServicesModel

CATEGORY_MAPPING = {
    'Notre histoire': 'Notre histoire',
    'Missions & valeurs': 'Missions & valeurs',
    'Attouts': 'Attouts',
    'Gouvernance': 'Gouvernance',
    'demande rse': 'demande rse',
    'certificat & labels': 'certificat & labels',
    'travail': 'travail',
    'formation intern': 'formation intern',
    'formation en cours': 'formation en cours',


}


class ArticlesByCategoryView(TemplateView):
    template_name = 'simple/home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name')
        actual_category_name = CATEGORY_MAPPING.get(category_name, category_name)
        context['published_articles'] = BekaModel.objects.filter(category=actual_category_name)
        context['temoins'] = ClientModel.objects.all()
        context['services'] = ServicesModel.objects.all()
        context['teams'] = EquipeModel.objects.all()

        return context
