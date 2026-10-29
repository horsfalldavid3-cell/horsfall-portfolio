from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core.sitemaps import HomeSitemap, ProjectSitemap


sitemaps = {
    "home": HomeSitemap,
    "projects": ProjectSitemap,
}


urlpatterns = [

    path("admin/", admin.site.urls),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    path("", include("core.urls")),

    path("projects/", include("projects.urls")),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
