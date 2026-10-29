from django.shortcuts import redirect, render

from .models import Profile, Skill, Service, Experience, ContactLink
from projects.models import Project
from contact.forms import ContactForm
from django.http import HttpResponse


def home(request):
    profile = Profile.objects.first()

    skills = Skill.objects.all()
    services = Service.objects.all()
    experiences = Experience.objects.all()
    contact_links = ContactLink.objects.filter(active=True)

    projects = Project.objects.filter(featured=True)

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect("contact_success")

    else:
        contact_form = ContactForm()

    context = {
        "profile": profile,
        "skills": skills,
        "services": services,
        "experiences": experiences,
        "projects": projects,
        "contact_form": contact_form,
    }

    return render(request, "home.html", context)


def contact_success(request):
    return render(request, "contact_success.html")

def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/

Sitemap: {}/sitemap.xml
""".format(request.build_absolute_uri("/").rstrip("/"))

    return HttpResponse(
        content,
        content_type="text/plain"
    )
