from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
import jdatetime
# Create your models here.


class PublishedPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = ("PB", "Published")
        DRAFT = ("DR", "Draft")

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=255,
        unique_for_date="publish",
        allow_unicode=True
    )
    body = models.TextField()
    author = models.ManyToManyField(
        settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status, default=Status.DRAFT)
    # tag
    tags = TaggableManager()

    # likes
    like = models.PositiveIntegerField(default=0)
    # managers
    objects = models.Manager()
    published = PublishedPost()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=["publish"])
        ]

    def get_absolute_url(self):
        return reverse("blog:post_details", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
        ])

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField("نام", max_length=40)
    author_email = models.EmailField("ایمیل")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField("متن")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f"Wrote by {self.author_name} for '{self.post}'"
