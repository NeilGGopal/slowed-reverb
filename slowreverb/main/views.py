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
    audio = yt.streams.filter(only_audio=True).first()
    audio.download('/Users/neilgopal/slowed-reverb/slowreverb/static/audio', url)  

    context['URL'] = "DOWNLOAD"    
    return render(request, 'home.html', context)