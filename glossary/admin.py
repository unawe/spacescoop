from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableModelForm
# from contrib.remainingcharacters.admin import CounterAdmin
from django.conf import settings
from django import forms

from .models import Entry


# class EntryAdminForm(TranslatableModelForm ):

#     class Meta:
#         model = Entry
#         fields = ['title', 'slug', 'code', 'short_description', 'description' ]
#         widgets = {
#             'short_description': forms.TextInput(attrs={'size':'180', }),
#         }

#     def clean_short_description(self):
#         short_description = self.cleaned_data['short_description']
#         short_description = short_description.replace('\n', ' ').strip()
#         return short_description


class EntryAdmin(TranslatableAdmin):
    # form = EntryAdminForm
    list_display = ('title', 'all_languages_column', )

    fieldsets = (
        (None,
            {'fields': ('title', 'slug', ), }),
        (None,
            {'fields': ('short_description', 'description', ), }),
    )

    readonly_fields = ('slug', )
    counted_fields = ('short_description', )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name is 'short_description':
            field.widget.attrs['size'] = 180
            field.widget.attrs['class'] = 'counted ' + field.widget.attrs.get('class', '')
        return field

    # def get_prepopulated_fields(self, request, obj=None):
    #     # can't use `prepopulated_fields = ..` because it breaks the admin validation
    #     # for translated fields. This is the official django-parler workaround.
    #     return {
    #         'slug': ('title',),
    #         'code': ('slug',),
    #     }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',
            'js/jquery.charCount.js',
        )

admin.site.register(Entry, EntryAdmin)
