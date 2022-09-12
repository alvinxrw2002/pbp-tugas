from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
katalog_data = CatalogItem.objects.all()
context = {
    'katalog_list' : katalog_data,
    'name' : 'Alvin Xavier Rakha Wardhana',
    'id' : 210750300
}

def show_katalog(request):
    return render(request, "katalog.html", context)