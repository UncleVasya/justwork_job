from django.core.management import BaseCommand
from django.core.management import call_command
from app.pages.models import ContentPiece, Page


class Command(BaseCommand):
    def handle(self, *args, **options):
        if ContentPiece.objects.exists() or Page.objects.exists():
            print('DB is not empty, no need to load initial data.')
            return

        print('DB is empty, loading initial data.')
        call_command('loaddata', 'initial_data')
