from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    protocol = 'https'
    priority = 1.0
    i18n = True

    def items(self):
        return ['index', 'about', 'privacy', 'tandc', 'faq', 'cutter', 'audio', 'without', 'watermark', 'audio_cutter'] # path's name
    def location(self, item):
        return reverse(item)