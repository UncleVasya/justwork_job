from django.test import TestCase
from app.pages.models import Page
from app.pages.tasks import update_page_counters


class UpdatePageCountersTest(TestCase):
    fixtures = ['initial_data']  # TODO: use factory_boy instead of fixtures

    def test_page_counters_update(self):
        page = Page.objects.filter(id=100).prefetch_related('pieces')[0]
        counters = [x.counter for x in page.pieces.all()]

        update_page_counters(page.pk)

        page.refresh_from_db()
        new_counters = [x.counter for x in page.pieces.all()]

        self.assertTrue(
            all(new == old + 1 for new in new_counters for old in counters)
        )
