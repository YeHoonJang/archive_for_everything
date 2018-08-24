from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

import pymysql
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
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        title = request.POST['title']
        print("file: ", file)
        fs = FileSystemStorage()
        print("fs: ", fs)
        filename = fs.save(file.name, file)
        print("filename: ", filename.split('.')[0])
        uploaded_file_url = fs.url(filename)
        print("url: ", uploaded_file_url)
        author = 'me'
        #pymysql 로 mysql 에 data insert
        conn = pymysql.connect(host='localhost', user='root', password='ini6223', db='django_db', charset='utf8')
        curs = conn.cursor()

        sql = "INSERT INTO relocations_contents VALUES (null, '%s', '%s', '%s', now(), 0)" % (title, uploaded_file_url, author)

        curs.execute(sql)
        conn.commit()
        curs.close()

        return render(request, 'relocations/upload.html',
                      {'uploaded_file_url':uploaded_file_url})
    return render(request, 'relocations/upload.html')