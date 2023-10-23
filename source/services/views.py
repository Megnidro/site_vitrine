from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import ServicesModel, ProjetModel


class ArticlesByCategoryView(ListView):
    template_name = 'services/service_liste.html'
    context_object_name = 'services'
    model = ServicesModel


class DetailArticleView(DetailView):
    model = ServicesModel
    template_name = 'index/politiques/detail.html'
    context_object_name = 'get_detail_article'


def projet(request):
    projets = ProjetModel.objects.all()

    context = {"projets": projets,

               }

    return render(request, 'simple/beka/lists.html', context)


class PrjetsByCategoryView(DetailView):
    model = ProjetModel
    template_name = 'simple/beka/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['published_articles'] = ProjetModel.objects.all()[:3]

        return context
