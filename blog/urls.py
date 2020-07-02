from django.urls import path

from blog.views import app1_l1, app1_l2,app1_l3

from blog.views import app2_link1,app2_link2,app2_link3
from blog.views import app3_link1,app3_link2,app3_link3

from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}




urlpatterns = [
    path('app1/link1/', app1_l1, name='app1l_ink1'),
    path('app1_link2/', app1_l2, name='app1_link2'),
    path('app1_link3/', app1_l3, name='app1_link3'),
    path('app2_link1', app2_link1, name='app2_link1'),
    path('app2_link2/', app2_link2, name='app2_link2'),
    path('app2_link3/', app2_link3, name='app2_link3'),
    path('app3_link1/', app3_link1, name='app3_link1'),
    path('app3_link2/', app3_link2, name='app3_link2'),
    path('app3_link3/', app3_link3, name='app3_link3'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
]