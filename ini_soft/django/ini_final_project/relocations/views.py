from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UploadFileForm
from django.contrib.auth.models import User
from django.contrib.auth import login

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
    content_route = str(Contents.objects.get(pk=vid).file)
    content_route = os.path.join(BASE_DIR, content_route)
    print(content_route)
    content_route_dict = {'content_route':content_route}
    return render(request, 'relocations/watching.html', content_route_dict)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('main')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
    return render(request, 'relocations/adduser.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        print("여기임")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("111111111111")
            form.save()
            return HttpResponseRedirect('success/url/')
        else:
            print("22222")
            form = UploadFileForm()
            return render(request, 'relocations/upload.html', {'form': form})
