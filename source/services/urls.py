from django.urls import path

from . import views
from .views import ArticlesByCategoryView, DetailArticleView, projet, PrjetsByCategoryView

app_name = 'services'

urlpatterns = [
    path('', ArticlesByCategoryView.as_view(),  name='service'),
    path('detail/<str:slug>/', DetailArticleView.as_view(), name='post'),
    path('projet/', projet, name='projet'),
    path('projets/<str:slug>/', PrjetsByCategoryView.as_view(), name='detail'),

]
