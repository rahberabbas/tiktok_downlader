from django.shortcuts import render, HttpResponse
from datetime import datetime
import os
from moviepy.editor import *
from .import functions
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def audio(request):
    return render(request, 'audio.html')

def download1(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "www.tiktok.com" in url:
            
            url = url
            rtr = functions.withwater_download(urls=url)
        else:
            return HttpResponse("Your link is Invalid")
        context={'url': url}
        return render(request, 'download1.html', context)
    else:
        return render(request, 'audio.html')

def downloadlink1(request):
    if url:
        data = rtr.content
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        with open(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4', 'wb') as f:
            f.write(data)

        video = VideoFileClip(os.path.join(BASE_DIR+"/audio_down",filename) + '.mp4')
        video.audio.write_audiofile(os.path.join(BASE_DIR+"/audio_down2",filename) + '.mp3')

        with open(os.path.join(BASE_DIR+"/audio_down2",filename+'.mp3'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/aud.mp3')
        response['Content-Disposition'] = 'attachment; filename="audio_tiksss.mp3"'
        return response
    else:
        return HttpResponse("Something Went Wrong")