from django.shortcuts import render
from django.http import HttpResponse
import pytube
from pydub import AudioSegment
from pysndfx import AudioEffectsChain

# Create your views here.

def home(request):
    context = {}
    url = request.GET.get('URL')

    if url == '' or url is None:
        return render(request, 'home.html')
    
    yt = pytube.YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download('/Users/neilgopal/slowed-reverb/slowreverb/static/audio', url[32:]) 

    mp4_audio = AudioSegment.from_file(f'/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:]}.mp4', "mp4")
    # slowed_audio = mp4_audio.low_pass_filter(800)
    mp4_audio.export(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:]}.wav", format="wav")

    fx = (
        AudioEffectsChain()
        .reverb()
        .speed(0.8)
    )

    fx(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:]}.wav", 
    f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:]}.wav")

    context['URL'] = "DOWNLOAD"    
    return render(request, 'home.html', context)