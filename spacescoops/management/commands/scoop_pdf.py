import sys

from django.core.management.base import BaseCommand
from django.conf import settings

from spacescoops.models import Article


class Command(BaseCommand):
    help = 'Generates PDF for the specified articles'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--code', help='Four digit code (YYnn) of the article')
        parser.add_argument('--lang', help='Language of the article')


    def handle(self, *args, **options):
        try:
            a = Article.objects.get(code=options['code'])
        except:
            self.stderr.write(f"Article {options['code']} not found")
            sys.exit()
        if options.get('lang',None):
            try:
                version = a.translations.get(language_code=options['lang'])
            except:
                self.stderr.write(f"Article {options['code']} in {options['lang']} not found")
                sys.exit()
            versions = [version]
        else:
            versions = a.translations.all()
        for version in versions:
            filename = version.generate_pdf()
            self.stdout.write(f'Written {filename}')
