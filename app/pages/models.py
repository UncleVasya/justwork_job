from django.db import models
from polymorphic.models import PolymorphicModel


class ContentPiece(PolymorphicModel):
    title = models.CharField(max_length=255)
    counter = models.PositiveIntegerField()


class TextPiece(ContentPiece):
    text = models.TextField()


class AudioPiece(ContentPiece):
    bitrate = models.PositiveSmallIntegerField()


class VideoPiece(ContentPiece):
    video_url = models.URLField()
    subtitles_url = models.URLField()


class Page(models.Model):
    pieces = models.ManyToManyField(ContentPiece)

