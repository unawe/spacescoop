from whoosh.fields import Schema, ID, TEXT
from whoosh.columns import RefBytesColumn
from whoosh.qparser import QueryParser, MultifieldParser, WildcardPlugin
from whoosh.analysis import StemmingAnalyzer, CharsetFilter
from whoosh.sorting import Facets, StoredFieldFacet, FieldFacet
from whoosh.support.charset import accent_map
from django.conf import settings

from django_ext.whoosh_utils import LanguageIndex
from spacescoops.models import Article


def _get_schema():
    analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)  # WARN: stemming is english specific; character folding is for western languages
    schema = Schema(
        code=ID(unique=True, stored=True),
        slug=ID(unique=False, stored=True),
        title=TEXT(analyzer=analyzer, stored=True),
        content=TEXT(analyzer=analyzer),
        )
    return schema


def _remove_html_tags(data):
    import re
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def _content(obj):
    return '\n\n\n'.join([
        # obj.title,
        _remove_html_tags(obj.story),
        # bleach.clean(obj.story, tags=None, strip=True),
        str(obj.cool_fact),
    ])


def rebuild_indexes():
    try:
        writers = {}
        # print("rebuild_indexes")
        for obj_master in Article.objects.available():
            for obj in obj_master.translations.all():
                lang = obj.language_code
                if lang not in writers:
                    ix = LanguageIndex(settings.WHOOSH_INDEX_PATH, lang, _get_schema())
                    ix.clear()
                    writers[lang] = ix.get_writer()
                _update_article(obj_master, obj, writer=writers[lang])
    finally:
        for writer in writers.values():
            writer.commit()


def _update_article(obj_master, obj, writer):
    writer.update_document(code=obj_master.code, slug=obj.slug, title=obj.title, content=_content(obj), )


def update_article(obj_master):
    indexes = LanguageIndexes()
    for obj in obj_master.translations.all():
        with indexes[obj.language_code].get_writer() as writer:
            _update_article(obj_master, obj, writer=writer)


def remove_article(obj):
    #TODO
    pass


def search(querystring, language_code):
    ix = LanguageIndex(settings.WHOOSH_INDEX_PATH, language_code, _get_schema()).load()
    # parser = QueryParser('content', ix.schema)
    parser = MultifieldParser(['title', 'keywords', 'content'], ix.schema)  # fieldboosts={'title':5, 'keywords':4, 'content':1})
    parser.remove_plugin_class(WildcardPlugin)  # remove unused feature for better performance
    query = parser.parse(querystring)
    # print(parser, query, querystring)

    result = {
        'results': [],
    }

    with ix.searcher() as searcher:
        results = searcher.search(query)
        # print(results)
        # import pdb; pdb.set_trace()

        # collect results
        for hit in results:
            my_hit = {}
            # my_hit['pos'] = hit.pos
            # my_hit['rank'] = hit.rank
            # my_hit['docnum'] = hit.docnum
            my_hit['score'] = hit.score
            my_hit['object'] = Article.objects.get(code=hit.fields()['code'])
            #.exclude(published=False).exclude(release_date__gte=datetime.today())
            # my_hit['object']['is_visible'] = True
            result['results'].append(my_hit)
            # print(hit.pos, hit.rank, hit.docnum, hit.score, hit)

    return result
