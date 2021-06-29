from django.shortcuts import render, HttpResponse
from datetime import datetime
import os
from .import function

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    return render(request, 'index.html')

def download(request):
    if request.method == "POST":
        global url
        global rtr
        url = request.POST.get('url')
        if "www.tiktok.com" in url:
            url = url
            rtr = function.withwater_download(urls=url)
        else:
            return HttpResponse("Your link is Invalid")
        context={'url': url}
        return render(request, 'download.html', context)
    else:
        return HttpResponse('Something went Wrong')

def downloadlink(request):
    if url:
        data = rtr.content
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        with open(os.path.join(BASE_DIR+"/video_down",filename) + '.mp4', 'wb') as f:
            f.write(data)

        with open(os.path.join(BASE_DIR+"/video_down",filename+'.mp4'), 'rb') as f:
            data = f.read()

        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = 'attachment; filename="video_tiksss.mp4"'
        return response
    else:
        return HttpResponse("Something Went Wrong")

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'privacypolicy.html')

def tandc(request):
    return render(request, 'tandc.html')

def faq(request):
    return render(request, 'faq.html')

def error_404_view(request, exception):
    return render(request, 'index.html')