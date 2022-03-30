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
    pieces = models.ManyToManyField(ContentPiece, through='PieceOnPage')


class PieceOnPage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    piece = models.ForeignKey(ContentPiece, on_delete=models.CASCADE)

