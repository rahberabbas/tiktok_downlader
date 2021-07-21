from django.shortcuts import render, HttpResponse
from datetime import datetime
import os
from moviepy.editor import *
from .import functions
import uuid
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def audio(request):
    return render(request, 'audio.html')

def download1(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "tiktok.com" in url:
            
            url = url
            rtr = functions.withwater_download(urls=url)
            r = uuid.uuid4().hex
            file_hello = f"tiksss_{r}.mp3"
            data = rtr.content
            filename = str(uuid.uuid4())
            with open(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4', 'wb') as f:
                f.write(data)

            video = VideoFileClip(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4')
            video.audio.write_audiofile(os.path.join(BASE_DIR+"/audio_down2",filename) + '.mp3')

            with open(os.path.join(BASE_DIR+"/audio_down2",filename+'.mp3'), 'rb') as f:
                data = f.read()
            time.sleep(7)
            response = HttpResponse(data, content_type='audio/webm')
            response['Content-Disposition'] = "attachment; filename=%s"  % file_hello
            return response
        else:
            return render(request, 'audio.html')
    else:
        return render(request, 'audio.html')

def downloadlink1(request):
    if url:
        r = uuid.uuid4()
        file_hello = f"tiksss.com_{r}.mp3"
        data = rtr.content
        filename = str(uuid.uuid4())
        with open(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4', 'wb') as f:
            f.write(data)

        video = VideoFileClip(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4')
        video.audio.write_audiofile(os.path.join(BASE_DIR+"/audio_down2",filename) + '.mp3')

        with open(os.path.join(BASE_DIR+"/audio_down2",filename+'.mp3'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/aud.mp3')
        response['Content-Disposition'] = "attachment; filename=%s"  % file_hello
        return response
    else:
        return HttpResponse("Something Went Wrong")