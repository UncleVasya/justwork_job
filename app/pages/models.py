from django.db import models
from polymorphic.models import PolymorphicModel


class ContentPiece(PolymorphicModel):
    title = models.CharField(max_length=255)
    counter = models.PositiveIntegerField(default=0, blank=True)


class TextPiece(ContentPiece):
    text = models.TextField()

    def __str__(self):
        return f'Text: {self.title}'


class AudioPiece(ContentPiece):
    bitrate = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Audio: {self.title}'


class VideoPiece(ContentPiece):
    video_url = models.URLField()
    subtitles_url = models.URLField()

    def __str__(self):
        return f'Video: {self.title}'


class Page(models.Model):
    title = models.CharField(max_length=255)
    pieces = models.ManyToManyField(ContentPiece, through='PieceOnPage')

    def __str__(self):
        return self.title


class PieceOnPage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    piece = models.ForeignKey(ContentPiece, on_delete=models.CASCADE)
    piece_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['piece_order']

