from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150)
    headline = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )
    cv = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True
    )
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    level = models.PositiveIntegerField(
        default=80,
        help_text="Skill level from 0 to 100."
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon name or CSS class."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-start_date", "order"]

    def __str__(self):
        return f"{self.position} - {self.company}"


class ContactLink(models.Model):
        platform = models.CharField(max_length=100)
        url = models.URLField()
        display_text = models.CharField(max_length=150, blank=True)
        icon = models.CharField(
            max_length=100,
            blank=True,
            help_text="Optional icon name or CSS class."
        )
        order = models.PositiveIntegerField(default=0)
        active = models.BooleanField(default=True)

        class Meta:
            ordering = ["order", "platform"]

        def __str__(self):
            return self.platform





