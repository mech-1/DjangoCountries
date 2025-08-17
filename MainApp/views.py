from django.http.response import Http404
from django.shortcuts import render

from MainApp.utils import json_from_file


# Create your views here.
def home(request):
    context = {'pagename': 'Django Countries Homepage'}

    return render(request, 'pages/index.html', context)


def countries_list(request):
    countries_items = json_from_file()
    context = {'pagename': 'Django Countries',
               'countries_items': countries_items,
               }

    return render(request, 'pages/countries_list.html', context)


def country_detail(request, id):
    context = {
        'pagename': 'Django Countries',
    }
    countries_items = json_from_file()
    if 0 < id <= len(countries_items):
        for i, countries_item in enumerate(countries_items, 1):
            if i == id:
                context['countries_item'] = countries_item
                break
    else:
        raise Http404

    return render(request, 'pages/country_detail.html', context)


def languages_list(request):
    countries_items = json_from_file()
    languages_items = set()
    for item in countries_items:
        for language in item['languages']:
            languages_items.add(language)
    context = {
        'pagename': 'Django Countries',
        'languages_items': sorted(languages_items),
    }

    return render(request, 'pages/languages_list.html', context)
