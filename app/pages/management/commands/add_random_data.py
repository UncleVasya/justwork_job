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
            try:
                start = ContentPiece.objects.last().id + 1
            except AttributeError:
                start = 1

            pieces = self.create_random_texts(start, num)
            pieces += self.create_random_audios(start, num)
            pieces += self.create_random_videos(start, num)

            # now create pages with random content
            self.create_pages_with_content(num, pieces)

    @staticmethod
    def create_random_texts(start, num):
        titles = ['Tutorial', 'News', 'Article', 'Movie review']

        # sadly bulk_create doesn't work for our models :(
        pieces = []
        for k in range(start, start + num):
            obj = TextPiece.objects.create(
                title=f'{random.choice(titles)} {k}',
                text=f'bla bla bla {k}'
            )
            pieces.append(obj)

        return pieces

    @staticmethod
    def create_random_audios(start, num):
        titles = ['Song', 'Lesson', 'Podcast']

        pieces = []
        for k in range(start, start + num):
            obj = AudioPiece.objects.create(
                title=f'{random.choice(titles)} {k}',
                bitrate=random.choice([96, 128, 256, 320])
            )
            pieces.append(obj)

        return pieces

    @staticmethod
    def create_random_videos(start, num):
        titles = ['Movie', 'Tutorial', 'Funny cats', 'Game stream']

        pieces = []
        for k in range(start, start + num):
            obj = VideoPiece.objects.create(
                title=f'{random.choice(titles)} {k}',
                video_url=f'https://justwork-tube.com/video/{k}',
                subtitles_url=f'https://justwork-tube.com/subtitles/{k}'
            )
            pieces.append(obj)

        return pieces

    @staticmethod
    def create_pages_with_content(num, content):
        max_pieces_on_page = 6
        titles = ['Content by Vasya', 'Stories by Vova', 'Interesting stuff']

        try:
            start = Page.objects.last().id + 1
        except AttributeError:
            start = 1

        for k in range(start, start + num):
            obj = Page.objects.create(
                title=f'{random.choice(titles)} {k}',
            )
            obj.pieces.set(
                random.choices(content,
                               k=random.choice(range(max_pieces_on_page)))
            )