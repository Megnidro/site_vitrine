# from django import views
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Actualite.models import Actualite

from services.models import ProjetModel

from settings.models import ClientModel

from carriere.models import OffreEmploi


def index(request):
    projets = ProjetModel.objects.all()
    posts = Actualite.objects.all()[:6]
    temoins = ClientModel.objects.all()
    context = {
        "projets": projets,
        "posts": posts,
        'temoins': temoins
    }
    return render(request, 'simple/home/index.html', context)


def contact(request):
    return render(request, 'simple/home/contact.html')


class BlogPlost(ListView):
    model = Actualite
    template_name = 'simple/blog/lists.html'
    paginate_by = 12
    context_object_name = 'posts'


"""class ArticlesByCategoryView(DetailView):
    template_name = 'simple/blog/detail.html'
    model = Actualite
    context_object_name = 'post'
"""

"""
def about(request):
    return render(request, 'simple/home/about.html')
"""


class ArticlesByCategoryView(DetailView):
    model = Actualite
    template_name = 'simple/blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['published_articles'] = Actualite.objects.all()[:3]

        return context


def offre(request):
    offres = OffreEmploi.objects.all()
    return render(request, 'simple/offres/liste.html', {"offres": offres})


class OffreDetail(DetailView):
    model = OffreEmploi
    template_name = 'simple/offres/detail.html'
    context_object_name = 'post'
