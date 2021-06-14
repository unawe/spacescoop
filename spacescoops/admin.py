import re

from django.conf import settings
from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm
from parler.widgets import SortedCheckboxSelectMultiple

from .models import Article, Image, OriginalNews, Category, DEFAULT_TRANSLATION_CREDITS


class OriginalNewsInlineAdmin(admin.TabularInline):
    model = OriginalNews
    fields = ('institution', 'url', )
    extra = 1


class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'all_languages_column', 'position', )
    list_editable = ('position', )

    fieldsets = (
        (None,
            {'fields': ('title', ), }),
    )

    def has_add_permission(self, request):
        return False


class ArticleImageInline(admin.TabularInline):
    model = Image
    fields = ('title', 'file', 'position', )
    min_num = 2
    extra = 1


class ArticleAdminForm(TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.language_code in DEFAULT_TRANSLATION_CREDITS:
            self.initial['translation_credit_text'] = DEFAULT_TRANSLATION_CREDITS[self.language_code]['text']
            self.initial['translation_credit_url'] = DEFAULT_TRANSLATION_CREDITS[self.language_code]['url']

    def clean_code(self):
        code = self.cleaned_data['code']
        if not re.match('^\w*\d{4}$', code):
            raise forms.ValidationError('The code should be four digits, in the format: YY##')
        return code

    class Meta:
        model = Article
        fields = ['code', 'title', 'release_date', 'published', 'featured', 'story', 'cool_fact', 'translation_credit_text', 'translation_credit_url', ]

        widgets = {
            'categories': SortedCheckboxSelectMultiple,
            #TODO: django-parler seems to be replacing the default css class when Meta is defined...
            'title': forms.TextInput(attrs={'class': 'vTextField', }),
            'translation_credit_text': forms.TextInput(attrs={'class': 'vTextField', }),
            'translation_credit_url': forms.TextInput(attrs={'class': 'vTextField', }),
        }


def _admin_datetime_format(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z') if dt else None


class ArticleAdmin(TranslatableAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = Article.add_prefetch_related(qs)
        return qs

    def release_date_fmt(self, obj):
        return _admin_datetime_format(obj.release_date)
    release_date_fmt.admin_order_field = 'release_date'
    release_date_fmt.short_description = 'Release Date'

    list_display = ('code', 'title', 'all_languages_column', 'is_released', 'release_date_fmt', 'published', 'featured', )
    date_hierarchy = 'release_date'
    search_fields = ('code', 'translations__title', )
    list_filter = ('original_news__name',)

    form = ArticleAdminForm

    inlines = (
        OriginalNewsInlineAdmin,
        ArticleImageInline,
    )

    fieldsets = [
        (None,
            {'fields': ('code', 'title', ), }),
        ('Publishing',
            {'fields': (('release_date', ),
                        ('published', 'featured', ),), }),
        (None,
            {'fields': ('story', 'cool_fact', 'pdf'), }),
        ('Translation credits',
            {'fields': ('translation_credit_text', 'translation_credit_url', )}),
    ]
    readonly_fields = ('creation_date', 'modification_date', 'is_released')


ArticleAdminForm.Meta.fields += ['categories', 'tags']
ArticleAdmin.fieldsets.append(
    (None,
        {'fields': ('categories', 'tags', ), }),
)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
