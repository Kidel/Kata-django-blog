from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

def blogIndex(request):
    queryset = models.Entry.objects.published()
    paginator = Paginator(queryset, 2) # Show 2 per page

    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entries = paginator.page(paginator.num_pages)

    is_paginated = paginator.num_pages > 1
    return render(request, 'myblog/home.html', {'object_list': entries, 'is_paginated': is_paginated})
    

def blogDetail(request, slug):
    entry = get_object_or_404(models.Entry, slug=slug)
    return render(request, 'myblog/post.html', {'object': entry})