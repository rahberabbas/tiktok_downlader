from django.contrib import admin
from django.urls import path
from video.views import index, download, downloadlink, about, privacy, tandc, faq
from audio.views import audio, download1, downloadlink1
from without.views import downloadlink2, without, download2
from cutter.views import cutter, download3, download4, downloadlink3
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
urlpatterns += i18n_patterns(
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('privacy-policy/', privacy, name='privacy'),
    path('terms-of-services/', tandc, name='tandc'),
    path('faq/', faq, name='faq'),
    path('tiktok-video-cutter-online/', cutter, name="cutter"),


    path('tiktok-download-with-watermark/', download, name='down'),
    path('downloadlink/', downloadlink, name='downloadlink'),
    path('downloadlink3/', downloadlink3, name='downloadlink3'),
    path('downloadlink2/', downloadlink2, name='downloadlink2'),
    path('tiktok-to-mp3-converter-online/', audio, name='audio'),
    path('tiktok-download-audio/', download1, name='down1'),
    path('downloadlink1/', downloadlink1, name='downloadlink1'),
    path('download-tiktok-video-without-watermark/', without, name='without'),
    path('tiktok-download-without-watermark/', download2, name='down2'),
    path('tiktok-video-cutter-online-convert/', download3, name='down3'),
    path('tiktok-cutter-link/', download4, name='down4'),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

handler404 = 'video.views.error_404_view'