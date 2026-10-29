from django.urls import path

from .views import project_detail


urlpatterns = [
    path("<slug:slug>/", project_detail, name="project_detail"),
]

