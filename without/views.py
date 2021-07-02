from django.shortcuts import render, HttpResponse
from .import functions
import os
from moviepy.editor import *
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def without(request):
    return render(request, 'without.html')

def download2(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "tiktok.com" in url:
            url = url
            rtr = functions.without(url=url)
        else:
            return HttpResponse("Your link is Invalid")
        context={'url': url}
        return render(request, 'download2.html', context)
    else:
        return HttpResponse('Something went Wrong')

def downloadlink2(request):
    if url:
        data = rtr.content
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')

        with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'wb') as f:
            f.write(data)

        with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = 'attachment; filename="without_watermark_tiksss.mp4"'
        return response
    else:
        return HttpResponse("Something Went Wrong")