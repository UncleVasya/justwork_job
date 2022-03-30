from django.core.management import BaseCommand
from app.pages.models import ContentPiece, TextPiece, AudioPiece, VideoPiece, Page
import random
from django.db import transaction


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-n', '--number',
                            nargs='?', type=int, default=100, const=100)

    def handle(self, *args, **options):
        num = options['number']

        with transaction.atomic():
            pieces = []
            try:
                start = ContentPiece.objects.last().id + 1
            except AttributeError:
                start = 1

            # sadly bulk_create doesn't work for our models :(
            for k in range(start, start + num):
                obj = TextPiece.objects.create(
                    title=f'{random.choice(["Tutorial", "News", "Article", "Movie review"])} {k}',
                    text=f'bla bla bla {k}'
                )
                pieces.append(obj)

            for k in range(start, start + num):
                obj = AudioPiece.objects.create(
                    title=f'{random.choice(["Song", "Lesson", "Podcast"])} {k}',
                    bitrate=random.choice([96, 128, 256, 320])
                )
                pieces.append(obj)

            for k in range(start, start + num):
                obj = VideoPiece.objects.create(
                    title=f'{random.choice(["Movie", "Tutorial", "Funny cats", "Game stream"])} {k}',
                    video_url=f'https://justwork-tube.com/video/{k}',
                    subtitles_url=f'https://justwork-tube.com/subtitles/{k}'
                )
                pieces.append(obj)

            # now create pages with random content
            try:
                start = Page.objects.last().id + 1
            except AttributeError:
                start = 1

            for k in range(start, start + num):
                obj = Page.objects.create(
                    title=f'{random.choice(["Content by Vasya", "Stories by Vova", "Interesting stuff"])} {k}',
                )
                obj.pieces.set(
                    random.choices(pieces,
                                   k=random.choice(range(6)))
                )
