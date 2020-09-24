import os

from django.conf import settings

from django_ext.compiler import PdfCompiler
from .models import Article


OUT_PATH = os.path.join(settings.MEDIA_ROOT, 'articles', 'download')
OUT_URL = os.path.join(settings.MEDIA_URL, 'articles', 'download')
PRINT_PREVIEW_URLPATH = 'scoops:print-preview'


def pdf_filename(obj):
    return 'spacescoop-%s%s-%s.pdf' % (obj.code, obj.language_code, obj.slug)


compiler = PdfCompiler(Article, OUT_PATH, OUT_URL, pdf_filename, PRINT_PREVIEW_URLPATH)


def make_pdf(code, lang, site_url=None):
    if not site_url:
        site_url = settings.SITE_URL
    compiler.make_pdf(code, lang, site_url)


def get_pdf(code, lang):
    return compiler.get_pdf(code, lang, 'scoops')
