from celery import shared_task
from django.db.models import F
from app.pages.models import Page


@shared_task
def update_page_counters(page_pk):
    page = Page.objects.get(pk=page_pk)
    page.pieces.update(
         counter=F('counter') + 1
    )
