from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('video_list', views.VideoList.as_view(), name='video_list'),
    path('video_info', views.VideoInfo.as_view(), name='video_info'),
    path('watching/<int:vid>', views.video_count, name='counts'),
]
