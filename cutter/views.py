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
def cutter(request):
    return render(request, 'cutter.html')

def download3(request):
    if request.method == "POST":
        global url
        global rtr
        global x
        url = request.POST.get('url')
        if "tiktok.com" in url:
            url = url
            rtr = functions.without(url=url)
            short = pyshorteners.Shortener()
            x = short.tinyurl.short(rtr)
            t1 = request.POST.get('t1')
            tt1 = int(t1)
            t2 = request.POST.get('t2')
            tt2 = int(t2)
            rts = functions.without(url=url)
            r = uuid.uuid4().hex
            file_hello = f"tiksss_{r}.mp4"
            filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
            ffmpeg_extract_subclip(filename=rts, t1=tt1, t2=tt2, targetname=(os.path.join(BASE_DIR+"/video_cut",filename) + '.mp4'))

            with open(os.path.join(BASE_DIR+"/video_cut",filename+'.mp4'), 'rb') as f:
                data = f.read()

            response = HttpResponse(data, content_type='video/mp4')
            response['Content-Disposition'] = "attachment; filename=%s" % file_hello
            return response
        else:
            return render(request, 'cutter.html')
    else:
        return render(request, 'cutter.html')

def download4(request):
    if request.method == "POST":
        global tt2
        global tt1
        t1 = request.POST.get('t1')
        tt1 = int(t1)
        t2 = request.POST.get('t2')
        tt2 = int(t2)
        rts = functions.without(url=url)
        r = uuid.uuid4()
        file_hello = f"tiksss.com_{r}.mp4"
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        ffmpeg_extract_subclip(filename=rts, t1=tt1, t2=tt2, targetname=(os.path.join(BASE_DIR+"/video_cut",filename) + '.mp4'))

        with open(os.path.join(BASE_DIR+"/video_cut",filename+'.mp4'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = "attachment; filename=%s" % file_hello
        return response
    else:
        return render(request, 'cutter.html')