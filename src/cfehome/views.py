from django.shortcuts import render, redirect
from visits.models import *
def home(request):
    links = request.path
    page_count = PageVisits.objects.all().count()
    link_count = PageVisits.objects.filter(path=links).count()
    PageVisits.objects.create(path=links)
    print(links)

    context={
        'links':links,
        'page_count':page_count,
        'link_count':link_count
    }
    return render(request,'home.html',context)