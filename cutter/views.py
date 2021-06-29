from django.shortcuts import render, HttpResponse
from datetime import datetime
import os
from .import functions
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def cutter(request):
    return render(request, 'cutter.html')

def download3(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "www.tiktok.com" in url:
            url = url
            rtr = functions.without(url=url)
        else:
            return HttpResponse("Your link is Invalid")
        context={'url': url, 'rtr': rtr}
        return render(request, 'download3.html', context)
    else:
        return HttpResponse('Something went Wrong')

def download4(request):
    if request.method == "POST":
        global tt2
        global tt1
        global pick
        t1 = request.POST.get('t1')
        tt1 = int(t1)
        t2 = request.POST.get('t2')
        tt2 = int(t2)
        pick = request.POST.get('pick')
        context = {'t1': tt1, 't2': tt2, 'rtr': rtr, 'pick': pick}
        print(context)
        return render(request, 'download4.html', context)
    else:
        return render(request, 'download4.html')

def downloadlink3(request):
    if rtr and pick == "mp4":
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        ffmpeg_extract_subclip(filename=rtr, t1=tt1, t2=tt2, targetname=(os.path.join(BASE_DIR+"/video_cut",filename) + '.mp4'))

        with open(os.path.join(BASE_DIR+"/video_cut",filename+'.mp4'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = 'attachment; filename="video_cutter_tiksss.mp4"'
        return response
    elif rtr and pick == "mp3":
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        ffmpeg_extract_subclip(filename=rtr, t1=tt1, t2=tt2, targetname=(os.path.join(BASE_DIR+"/video_cut",filename) + '.mp4'))

        clip = VideoFileClip(os.path.join(BASE_DIR+"/video_cut",filename+'.mp4'))
        clip.audio.write_audiofile(os.path.join(BASE_DIR+"/audio_cut",filename+'.mp3'))

        with open(os.path.join(BASE_DIR+"/audio_cut",filename+'.mp3'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/audio.mp3')
        response['Content-Disposition'] = 'attachment; filename="audio_cutter_tiksss.mp3"'
        return response
    else:
        return HttpResponse("Something Went Wrong")
