from unittest.mock import patch
import debug_toolbar
from django.db import transaction, connection, connections
from django.test.utils import CaptureQueriesContext
from django.urls import path, include, reverse
from rest_framework import routers, status
from rest_framework.test import APITestCase, URLPatternsTestCase
from app.pages import apiviews
from app.pages.models import PieceOnPage, Page, TextPiece, AudioPiece


router = routers.DefaultRouter()
router.register(r'pages', apiviews.PageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


@patch('app.pages.tasks.update_page_counters.delay')
class ApiTests(APITestCase, URLPatternsTestCase):
    fixtures = ['initial_data']  # TODO: use factory_boy instead of fixtures
    urlpatterns = urlpatterns

    def test_paging(self, *args, **kwargs):
        page_size = 50
        test_data_size = Page.objects.count()

        url = reverse('page-list')
        response = self.client.get(url, format='json')
        items = response.data['results']

        self.assertEqual(response.data['count'], test_data_size)
        self.assertEqual(len(items), page_size)

    def test_content_order(self, *args, **kwargs):
        url = reverse('page-detail', kwargs={'pk': 100})

        # get initial last item
        response = self.client.get(url, format='json')
        old_last = response.data['pieces'][-1]

        # switch up items a little bit
        item = PieceOnPage.objects.filter(page__id=100).first()
        item.piece_order += 1000
        item.save()

        # check that last item has changed
        response = self.client.get(url, format='json')
        new_last = response.data['pieces'][-1]

        self.assertNotEqual(old_last, new_last)

    def test_readonly(self, *args, **kwargs):
        url = reverse('page-list')

        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        url = reverse('page-detail', kwargs={'pk': 0})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_page_counters_called(self, update_page_counters):
        url = reverse('page-detail', kwargs={'pk': 0})
        self.client.get(url, format='json')

        self.assertTrue(update_page_counters.called)


@patch('app.pages.tasks.update_page_counters.delay')
class ApiOptimizationTests(APITestCase, URLPatternsTestCase):
    pieces_num = 100
    max_allowed_queries = 6

    urlpatterns = urlpatterns

    @classmethod
    def setUpTestData(cls):
        # let's create a page with LOTS of content
        with transaction.atomic():
            page = Page.objects.create(title='test')
            pieces = []
            for k in range(cls.pieces_num):
                p = TextPiece.objects.create(
                    page=page,
                    title=f'text {k}',
                    text=f'bla bla'
                )
                pieces.append(p)
            page.pieces.set(pieces)
            cls.page = page

    def test_page_detail_optimized(self, *args, **kwargs):
        url = reverse('page-detail', kwargs={'pk': self.page.pk})

        capturer = CaptureQueriesContext(connection)
        with capturer:
            self.client.get(url)

        self.assertLessEqual(len(capturer.captured_queries), self.max_allowed_queries)
