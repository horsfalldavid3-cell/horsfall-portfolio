
from django.contrib import admin
from .models import Profile, Skill, Service, Experience, ContactLink


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "email", "updated_at")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level", "order")
    list_filter = ("category",)
    search_fields = ("name", "category")
    ordering = ("order", "name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    search_fields = ("title", "description")
    ordering = ("order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "start_date",
        "end_date",
        "current",
    )
    list_filter = ("current", "company")
    search_fields = ("position", "company")
    ordering = ("-start_date",)


@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "display_text",
        "active",
        "order",
    )
    list_filter = ("active",)
    search_fields = ("platform", "display_text")
    ordering = ("order", "platform")
