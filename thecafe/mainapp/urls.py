
from django.urls import path
from . import views
from .sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('', views.carousels, name='homepage'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap')
]
