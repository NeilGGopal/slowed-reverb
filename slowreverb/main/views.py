from __future__ import unicode_literals
import youtube_dl
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pydub import AudioSegment
from pysndfx import AudioEffectsChain
from pytube import YouTube
import os
import moviepy.editor as mp
import time

# Create your views here.

# Homepage for the application


def home(request, option):
    context = {}    # parameters to be sent to HTML
    context['URL'] = ""
    url = request.GET.get('URL')
    url_name = request.resolver_match.view_name

    if url == '' or url is None:
        return render(request, 'home.html')  # main page without audio

    # file path
    parent_dir = '/Users/neilgopal/slowed-reverb/slowreverb/static/audio'             
    # audio path
    path = f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4"
    # mp3 result path
    new_path = f'{parent_dir}/{url[32:43]}.mp3'

    if "download" == option:
        try:
            # remove downloaded file
            time.sleep(0.5)
            os.remove(
                f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.mp3")
        except FileNotFoundError:
            return render(request, 'home.html', context)
        context['URL'] = f"res-{url[32:43]}.mp3"
        # converted audio displayed on page
        return render(request, 'home.html', context)

    # if user chose conversion option
    if "convert" == option:
        if os.path.exists(f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.mp3"):
            context['URL'] = f"res-{url[32:43]}.mp3"
            # converted audio displayed on page
            return render(request, 'home.html', context)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{parent_dir}/{url[32:43]}.webm',
            'nocheckcertificate': True,
            'keepvideo': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{url}'])

        # yt = YouTube(url)
        # try:
        #     yt.streams.filter(only_audio=True, file_extension='mp4').first().download(parent_dir, url[32:43]) # downloads file to parent_dir as mp4
        # except:
        #     yt.streams.filter(file_extension='mp4').first().download(parent_dir, url[32:43])
        # clip = mp.AudioFileClip(path)
        # clip.write_audiofile(new_path)
        # clip.close()    # converts mp4 to mp3

        fx = (
            AudioEffectsChain()
            .reverb(reverberance=30)
            .speed(0.85)
        )   # applies effects

        # final file is downloaded
        fx(new_path,
           f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/res-{url[32:43]}.mp3")
        try:
            os.remove(
                f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp3")
            os.remove(
                f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.webm")
            os.remove(
                f"/Users/neilgopal/slowed-reverb/slowreverb/static/audio/{url[32:43]}.mp4")
        except FileNotFoundError:
            pass

    context['URL'] = f"res-{url[32:43]}.mp3"
    # converted audio displayed on page
    return render(request, 'home.html', context)
