from django.urls import path
from .views import home, contact_success, robots_txt


urlpatterns = [
    path("", home, name="home"),
    path(
        "contact/success/",
        contact_success,
        name="contact_success"
    ),
    path("robots.txt", robots_txt, name="robots_txt"),
]