from django.core.management.base import BaseCommand

from spacescoops.tasks import populate_article_count


class Command(BaseCommand):
    help = 'Populates aggregate fields'

    def handle(self, *args, **options):
        populate_article_count()
