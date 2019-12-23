from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from . import urls


class PostSitemap(Sitemap):
    priority = 1
    changefreq = 'weekly'
    protocol = "https"

    def items(self):
        return['homepage']

    def location(self, item):
        return reverse(item)
