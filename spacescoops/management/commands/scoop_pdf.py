import sys
import tempfile
import base64

from django.db.models import Q
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from spacescoops.models import Article, ArticleTranslation


class Command(BaseCommand):
    help = 'Generates PDF for the specified articles'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--code', help='Four digit code (YYnn) of the article, will replace existing PDFs unless used with --new')
        parser.add_argument('--lang', help='Language of the article')
        parser.add_argument(
            '--new',
            action='store_true',
            help='Generate PDFs for new scoops',
        )


    def handle(self, *args, **options):
        if options['new'] and not options['code']:
            versions = ArticleTranslation.objects.filter(Q(pdf='')|Q(pdf=None)).order_by('-creation_date')
        elif options['code']:
            try:
                a = Article.objects.get(code=options['code'])
                versions = a.translations.all()
            except:
                self.stderr.write(f"Article {options['code']} not found")
                sys.exit()
        else:
            self.stderr.write("Either select --new or enter --code or both")
            sys.exit()
        if options.get('lang',None):
            try:
                version = versions.get(language_code=options['lang'])
            except:
                self.stderr.write(f"Article {options['code']} in {options['lang']} not found")
                sys.exit()
            versions = [version]
        self.stdout.write(f'Generating PDFs for {len(versions)} scoops')
        for version in versions:
            if options['new'] and version.pdf:
                self.stdout.write(f"Skipping {version.master.code} in {version.language_code}")
                continue
            try:
                file_obj = version.generate_pdf()
            except Exception as e:
                self.stederr.write(f"{e}")
                self.stederr.write(f"Failed to create  {version.master.code} in {version.language_code}")
            filename = f'scoop-{version.master.code}-{version.language_code}.pdf'
            version.pdf.delete(save=False)
            version.pdf.save(filename, ContentFile(file_obj))
            version.save()
            self.stdout.write(f'Written {filename}')
