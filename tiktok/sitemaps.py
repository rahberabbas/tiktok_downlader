from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    i18n = True

    def items(self):
        return ['index', 'about', 'privacy', 'tandc', 'faq', 'cutter', 'down', 'audio', 'without'] # path's name
    def location(self, item):
        return reverse(item)