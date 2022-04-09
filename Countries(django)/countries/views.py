from django.shortcuts import render
from django.http import HttpResponse
from .models import Country2
from django.views.generic import ListView,DetailView

# def countab(request):
#     return render(request, 'countries/home.html')

class CountryListView(ListView):
    model = Country2
    context_object_name = 'count'
    template_name = 'countries\country_info_list.html'

class CountryDetailView(DetailView):
    model = Country2
    template_name = 'countries\country_info_detail.html'
    
def search(request):
    if request.method == 'POST':
        searchValue = request.POST['searchValue']
        filtered = Country2.objects.filter(name__icontains=searchValue)
        word = 'There is no result for the searched values.'
        empty = 'Please Fill In The Field.'

        if searchValue == '':
            return render(request, 'countries/searched.html', {'empty': empty})
        else:
            if len(filtered) < 1:
                return render(request, 'countries/searched.html', {'word': word})
            else:
                return render(request, 'countries/searched.html', {'searchValue':searchValue,'filtered':filtered} )
    
    else:
        return render(request, 'countries/searched.html')

def by_region(request):
    if request.method == 'POST':
        filter_region = request.POST['filter_region']

        if filter_region == 'Others':
            returned_filter = Country2.objects.filter(region = '')
        else:
            returned_filter = Country2.objects.filter(region = filter_region)
        return render(request, 'countries/filtered.html',{'returned_filter':returned_filter, 'filter_region':filter_region} )
    else:
        return render(request, 'countries/filtered.html')