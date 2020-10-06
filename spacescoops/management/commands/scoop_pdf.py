import os

from django.core.management.base import BaseCommand
from django.conf import settings

from spacescoops.pdfrender import Renderer


class Command(BaseCommand):
    help = 'Generates PDF for the specified articles'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('code', help='Four digit code (YYnn) of the article')
        parser.add_argument('lang', help='Language of the article')

        # Named (optional) arguments
        parser.add_argument(
            '--site-url',
            action='store',
            dest='site_url',
            default=None,
            help='Connect to a website other than %s' % settings.SITE_URL)

    def handle(self, *args, **options):
        DESTFOLDER = os.path.join(settings.MEDIA_ROOT, 'pdf')
        renderer = Renderer()
        renderer.run(DESTFOLDER)
