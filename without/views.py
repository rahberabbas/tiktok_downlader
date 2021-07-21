from django.shortcuts import render, HttpResponse
from .import functions
import os
from moviepy.editor import *
from datetime import datetime
import uuid

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
            r = uuid.uuid4().hex
            file_hello = f"tiksss_{r}.mp4"
            data = rtr.content
            filename = str(uuid.uuid4())

            with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'wb') as f:
                f.write(data)

            with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'rb') as f:
                data = f.read()

            response = HttpResponse(data, content_type='application/vnd.mp4')
            response['Content-Disposition'] = "attachment; filename=%s" % file_hello
            return response
        else:
            return render(request, 'without.html')
    else:
        return render(request, 'without.html')

def downloadlink2(request):
    if url:
        r = uuid.uuid4()
        file_hello = f"tiksss.com_{r}.mp4"
        data = rtr.content
        filename = str(uuid.uuid4())

        with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'wb') as f:
            f.write(data)

        with open(os.path.join(BASE_DIR+"/without_video",filename+'.mp4'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = "attachment; filename=%s" % file_hello
        return response
    else:
        return HttpResponse("Something Went Wrong")