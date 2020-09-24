from django.views.generic import ListView, DetailView
from parler.views import TranslatableSlugMixin

from .models import Entry


def _entry_queryset(qs, only_translations=True):
    if only_translations:
        qs = qs.active_translations()
    qs = qs.prefetch_related('translations')
    return qs


class EntryListView(ListView):
    model = Entry

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('translations__title')
        return _entry_queryset(qs)


class EntryDetailView(TranslatableSlugMixin, DetailView):
    model = Entry

    def get_language_choices(self):
        return [self.get_language(), 'en']  # TODO: nasty hack!

    def get_queryset(self):
        return _entry_queryset(super().get_queryset(), only_translations=False)
