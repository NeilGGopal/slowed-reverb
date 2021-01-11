from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pytube
import os
from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import mimetypes
from wsgiref.util import FileWrapper

# Create your views here.

def home(request, option):
    context = {}
    url = request.GET.get('URL')
    url_name = request.resolver_match.view_name

    if url == '' or url is None:
        return render(request, 'home.html')

    path = f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:]}.wav"    
    
    if "convert" == option:
        yt = pytube.YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download('/Users/neilgopal/slowed-reverb/slowreverb/static/audio', url[32:]) 

        mp4_audio = AudioSegment.from_file(f'/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:]}.mp4', "mp4")
        # slowed_audio = mp4_audio.low_pass_filter(800)
        mp4_audio.export(path, format="wav")

        fx = (
            AudioEffectsChain()
            .reverb()
            .speed(0.8)
        )

        fx(path, f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:]}.wav")

    elif "download" in url_name:
        pass

    context['URL'] = f"res-{url[32:]}.wav"
    return render(request, 'home.html', context)