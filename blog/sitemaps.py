from django.contrib.sitemaps import Sitemap
from .models import Post
from taggit.models import Tag
from django.urls import reverse
import urllib
# sitemap for posts


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, item):
        return item.updated


# also sitemaps for tags
class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Tag.objects.all()

    def location(self, item):
        return urllib.parse.unquote(reverse("blog:post_by_tag", args=[item.slug]))
