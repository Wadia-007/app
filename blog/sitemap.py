from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"
    def items(self):
        return Post.objects.filter(status="P")

    def lastmod(self,obj):
        return obj.date

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return ['about', 'advertise', 'contact','editorial','privacy','tc']

    def location(self, item):
        return reverse(item)




