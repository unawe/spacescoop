from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .forms import SearchForm
from spacescoops.models import ArticleTranslation, Article

import logging

logger = logging.getLogger(__name__)

def simplesearch(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = SearchQuery(form.cleaned_data['q'])
        vector = SearchVector('title','story', 'cool_fact')
        search_result = ArticleTranslation.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        context = {
            'query': query,
            'page': {'object_list': search_result[:10]},
            'request': request,
            'form': form,
        }
    else:
        context = {
            'request': request,
            'form': form,
        }

    if 'page' not in context or not context['page']['object_list']:
        context['featured'] = Article.objects.featured().active_translations()[0:3]
    return render(request, 'search/search.html', context)
