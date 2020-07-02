from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['app1_link1','app1_link2','app1_link3','app2_link1','app2_link2','app2_link3','app3_link1','app3_link2','app3_link3']
    def location(self, item):
        return reverse(item)