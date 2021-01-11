from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    url = request.GET.get('URL')

    if url == '' or url is None:
        return render(request, 'home.html')

    context['URL'] = "DOWNLOAD"    
    return render(request, 'home.html', context)