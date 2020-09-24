from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFieldsModel
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


class Entry(TranslatableModel):
    # code = models.SlugField(unique=True, max_length=255, help_text='The code must be unique, and identical to the english Slug. Do not translate!')
    # translations = TranslatedFields(
    #     slug = models.SlugField(unique=True, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.'),
    #     title = models.CharField(_('title'), max_length=255),
    #     short_description = models.CharField(max_length=180),
    #     description = RichTextField(),
    # )

    def is_translation_fallback(self):
        return not self.has_translation(self.language_code)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('glossary:detail', kwargs={'slug': self.slug, })

    class Meta:
        verbose_name_plural = 'entries'
        # ordering = ('translations__title', )  # this setting causes the admin to break


class EntryTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Entry, related_name='translations', null=True, on_delete=models.CASCADE)
    slug = AutoSlugField(max_length=200, populate_from='title', always_update=True, unique_with=('language_code',))
    # slug = models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')
    title = models.CharField(_('title'), max_length=200)
    short_description = models.CharField(max_length=180)
    description = RichTextField(blank=True, null=True)

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'slug'),
        )
