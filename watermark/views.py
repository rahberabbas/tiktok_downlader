import time
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
import os
from .import function
import uuid


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def watermark(request):
    return render(request, 'watermark.html')

def download8(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "tiktok.com" in url:
            url = url
            rtr = function.withwater_download(urls=url)
            r = uuid.uuid4()
            file_hello = f"tiksss.com_{r}.mp4"
            data = rtr.content
            filename = str(uuid.uuid4())
            with open(os.path.join(BASE_DIR+"/video_down",filename) + '.mp4', 'wb') as f:
                f.write(data)
            
            with open(os.path.join(BASE_DIR+"/video_down",filename+'.mp4'), 'rb') as f:
                data = f.read()
            time.sleep(7)
            response = HttpResponse(data, content_type='application/vnd.mp4')
            response['Content-Disposition'] = "attachment; filename=%s" % file_hello
            return response
        else:
            return render(request, 'watermark.html')
    else:
        return render(request, 'watermark.html')