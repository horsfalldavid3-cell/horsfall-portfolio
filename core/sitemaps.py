from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from projects.models import Project


class HomeSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse("home")


class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("project_detail", kwargs={"slug": obj.slug})
