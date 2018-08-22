from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
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


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse('로그인 실패! 다시 시도 해보십시오.')
    else:
        form = LoginForm()
        return render(request, 'relocations/login.html', {'form': form})