from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchList

# Create your views here.
def show_watchlist(request):
    watch_list = WatchList.objects.all()
    context = {
        'my_watch_list' : watch_list,
        'name' : 'Alvin Xavier Rakha Wardhana',
        'id' : 210750300
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")