from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchList

# Create your views here.
def show_watchlist(request):
    watch_list = WatchList.objects.all()

    # Count amount of watched movies
    watched_amnt = 0
    for watch in watch_list:
        if watch.watched == "V":
            watched_amnt += 1

    # Watched many or few
    banyak_nonton = "Wah, kamu masih sedikit menonton!"
    if watched_amnt >= 5:
        banyak_nonton = "Selamat, kamu sudah banyak menonton!"

    context = {
        'my_watch_list' : watch_list,
        'name' : 'Alvin Xavier Rakha Wardhana',
        'id' : 210750300,
        'jumlah_tontonan' : banyak_nonton
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")