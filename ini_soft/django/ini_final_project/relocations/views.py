from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
import redis
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from .models import Contents

def main(request):
    return render(request, 'relocations/main.html')


class VideoList(generic.ListView):
    template_name = 'relocations/video_list.html'
    context_object_name = 'contents_list'

    def get_queryset(self):
        return Contents.objects.values()

class VideoInfo(generic.ListView):
    template_name = 'relocations/video_info.html'
    context_object_name = 'content_info_list'

    def get_queryset(self):
        return Contents.objects.values()


#redis에 data 어떻게 넣지???
def video_count(request, vid):
    selected_video = Contents.objects.get(pk=vid)
    selected_video.counts += 1
    selected_video.save()
    # rc = redis.Redis(host='192.168.10.37', port=6379, db=0)
    # print("keys:", rc.keys())
    content_route = str(Contents.objects.get(pk=vid).content_file)
    content_route = os.path.join(BASE_DIR, content_route)
    content_route = os.path.join('192.168.10.37:', content_route)
    content_route_dict = {'content_route':content_route}
    return render(request, 'relocations/watching.html', content_route_dict)
