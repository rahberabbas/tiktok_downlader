from django.shortcuts import render, HttpResponse
from datetime import datetime
import os
import pyshorteners
from .import functions
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def audio_cutter(request):
    return render(request, 'audio_cutter.html')

def download5(request):
    if request.method == "POST":
        global url
        global rtr
        global x
        url = request.POST.get('url')
        if "www.tiktok.com" in url:
            url = url
            rtr = functions.without(url=url)
            short = pyshorteners.Shortener()
            x = short.tinyurl.short(rtr)
        else:
            return HttpResponse("Your link is Invalid")
        context={'url': url, 'rtr': rtr, 'x': x}
        return render(request, 'download3.html', context)
    else:
        return HttpResponse('Something went Wrong')

def download6(request):
    if request.method == "POST":
        global tt2
        global tt1
        t1 = request.POST.get('t1')
        tt1 = int(t1)
        t2 = request.POST.get('t2')
        tt2 = int(t2)
        context = {'t1': tt1, 't2': tt2, 'rtr': rtr,}
        r = uuid.uuid4()
        file_hello = f"tiksss.com_{r}.mp3"
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        ffmpeg_extract_subclip(filename=rtr, t1=tt1, t2=tt2, targetname=(os.path.join(BASE_DIR+"/video_cut",filename) + '.mp4'))

        clip = VideoFileClip(os.path.join(BASE_DIR+"/video_cut",filename+'.mp4'))
        clip.audio.write_audiofile(os.path.join(BASE_DIR+"/audio_cut",filename+'.mp3'))

        with open(os.path.join(BASE_DIR+"/audio_cut",filename+'.mp3'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/audio.mp3')
        response['Content-Disposition'] = "attachment; filename=%s" % file_hello
        return response
    else:
        return render(request, 'download5.html')