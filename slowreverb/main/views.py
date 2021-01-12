from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import pytube
import os

# Create your views here.

# Homepage for the application
def home(request, option):
    context = {}    # parameters to be sent to HTML
    context['URL'] = ""
    url = request.GET.get('URL')
    url_name = request.resolver_match.view_name

    if url == '' or url is None:
        return render(request, 'home.html') # main page without audio

    path = f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.wav" # audio path    
    
    # if user chose conversion option
    if "convert" == option:
        yt = pytube.YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download('/Users/neilgopal/slowed-reverb/slowreverb/static/audio', url[32:43]) 

        mp4_audio = AudioSegment.from_file(f'/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4', "mp4")
        mp4_audio.export(path, format="wav")

        fx = (
            AudioEffectsChain()
            .reverb()
            .speed(0.8)
        )   # applies effeects

        fx(path, f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.wav")    # final file is downloaded
        os.remove(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.wav")
        os.remove(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4")
        

    context['URL'] = f"res-{url[32:43]}.wav"
    return render(request, 'home.html', context)    # converted audio displayed on page