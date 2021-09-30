from django.db import models
import uuid
from datetime import datetime


class Website(models.Model):
    name = models.CharField(max_length=200)
    main_url = models.CharField(max_length=200)
    rss_url = models.CharField(max_length=200, null=False)
    rss_item_node = models.CharField(max_length=20, null=False, blank=True)
    news_title_field = models.CharField(max_length=20, null=False, blank=True)
    news_link_field = models.CharField(max_length=20, null=False, blank=True)
    news_content_field = models.CharField(max_length=20, null=False, blank=True)
    news_published_field = models.CharField(max_length=20, null=False, blank=True)
    news_author_field = models.CharField(max_length=20, null=False, blank=True)
    news_guid_field = models.CharField(max_length=20, null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=False, blank=True, default=datetime.now)
    aggregated = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, null=False, default="")
    guid = models.CharField(max_length=100, null=False, default="")
    clicks_on_source = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-published']

    @property
    def track_click(self):
        self.clicks_on_source += 1
        self.save()
