from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import pytube
import os
import moviepy.editor as mp

# Create your views here.

# Homepage for the application
def home(request, option):
    context = {}    # parameters to be sent to HTML
    context['URL'] = ""
    url = request.GET.get('URL')
    url_name = request.resolver_match.view_name

    if url == '' or url is None:
        return render(request, 'home.html') # main page without audio

    parent_dir = '/Users/neilgopal/slowed-reverb/slowreverb/static/audio'             # file path
    path = f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4" # audio path
    new_path = f'{parent_dir}/{url[32:43]}.mp3'                                       # mp3 result path
    
    if "download" == option:
        os.remove(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.mp3") # remove downloaded file 
        context['URL'] = f"res-{url[32:43]}.mp3"
        return render(request, 'home.html', context)    # converted audio displayed on page   

    # if user chose conversion option
    if "convert" == option:
        yt = pytube.YouTube(url)
        audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(parent_dir, url[32:43])      # downloads file to parent_dir as mp4

        clip = mp.AudioFileClip(path)
        clip.write_audiofile(new_path)
        clip.close()    # converts mp4 to mp3

        fx = (
            AudioEffectsChain()
            .reverb()
            .speed(0.8)
        )   # applies effects

        fx(new_path, f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.mp3")    # final file is downloaded
        os.remove(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp3")
        os.remove(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4") 
    
    context['URL'] = f"res-{url[32:43]}.mp3"
    return render(request, 'home.html', context)    # converted audio displayed on page