from django.db import IntegrityError
from django.test import TestCase

from app.pages.models import TextPiece, AudioPiece, VideoPiece, ContentPiece


class ContentPieceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        TextPiece.objects.create(title='Tutorial', text='bla bla bla')
        AudioPiece.objects.create(title='Xandria - Salome', bitrate=128)
        VideoPiece.objects.create(
            title=f'Test video',
            video_url=f'https://justwork-tube.com/video/42',
            subtitles_url=f'https://justwork-tube.com/subtitles/42'
        )

    def test_pieces_amount(self):
        # checks that base polymorphic model sees all its children
        self.assertEqual(3, ContentPiece.objects.count())

    def test_title_is_unique_for_piece_type(self):
        try:
            # same song, but adding video this time
            VideoPiece.objects.create(title='Xandria - Salome')
        except IntegrityError:
            self.fail('Creating different content with same title should be allowed.')

        with self.assertRaises(IntegrityError):
            # creating same song twice
            AudioPiece.objects.create(title='Xandria - Salome')

    def test_common_polymorphic_fields(self):
        self.assertTrue(
            all(hasattr(piece, field) for piece in ContentPiece.objects.all()
                                      for field in ['title', 'counter'])
        )

    def test_video_polymorphic_fields(self):
        specific_fields = ['video_url', 'subtitles_url']

        video = ContentPiece.objects.get(title='Test video')
        self.assertTrue(
            all(hasattr(video, attr) for attr in specific_fields)
        )
