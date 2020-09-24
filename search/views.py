from django.shortcuts import render

from . import whoosh_utils
from .forms import SearchForm


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['q']
        search_result = whoosh_utils.search(search_query, request.LANGUAGE_CODE)
        context = {
            'query': search_query,
            'page': {'object_list': search_result['results']},
            'request': request,
            'form': form,
        }
    else:
        context = {
            'request': request,
            'form': form,
        }

    return render(request, 'search/search.html', context)
