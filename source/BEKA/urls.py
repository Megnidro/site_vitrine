from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from contact.views import contact_offre
from .views import index, contact, ArticlesByCategoryView, BlogPlost, offre, OffreDetail

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contact/',  contact, name='contact'),
    path('blog/', BlogPlost.as_view(), name='blog'),
    path('blog/<str:slug>/', ArticlesByCategoryView.as_view(), name='detail'),
    path('services/', include('services.urls')),
    path('beka/', include('settings.urls')),
    path('contact/', contact, name="contact"),
    path('depot-candidature/', contact_offre, name="contact_offre"),
    path('offre-d-employment/', offre, name="offre"),
    path('offre-emploi-detail/<str:slug>/', OffreDetail.as_view(), name='offre-detail'),

]
