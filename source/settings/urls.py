from django.urls import path

from .views import ArticlesByCategoryView

urlpatterns = [
    path('notre-histoire/', ArticlesByCategoryView.as_view(), {'category_name': 'Notre histoire'}, name='history'),
    path('missions-valeurs/', ArticlesByCategoryView.as_view(), {'category_name': 'Missions & valeurs'},
         name='missions'),
    path('nos-attouts/', ArticlesByCategoryView.as_view(), {'category_name': 'Attouts'}, name='attouts'),
    path('gouvernance/', ArticlesByCategoryView.as_view(), {'category_name': 'Gouvernance'}, name='gouvernance'),
    path('demande-rse/', ArticlesByCategoryView.as_view(), {'category_name': 'demande rse'}, name='demande'),
    path('certificat-label/', ArticlesByCategoryView.as_view(), {'category_name': 'certificat & labels'},
         name='certficats'),
    path('travailler-chez-beka/', ArticlesByCategoryView.as_view(), {'category_name': 'travail'}, name='travail'),
    path('formation-interne/', ArticlesByCategoryView.as_view(), {'category_name': 'formation intern'}, name='formationinterne'),
    path('formation-en-cours-etude/', ArticlesByCategoryView.as_view(), {'category_name': 'formation en cours'}, name='formation'),

]
