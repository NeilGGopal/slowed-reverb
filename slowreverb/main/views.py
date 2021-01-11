from django.shortcuts import render
from django.http import HttpResponse
import pytube

# Create your views here.

def home(request):
    context = {}
    url = request.GET.get('URL')

    if url == '' or url is None:
        return render(request, 'home.html')
    
    yt = pytube.YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download('/Users/neilgopal/slowed-reverb/static/audio')  

    context['URL'] = "DOWNLOAD"    
    return render(request, 'home.html', context)