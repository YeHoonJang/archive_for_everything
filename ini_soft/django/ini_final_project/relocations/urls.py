from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('video_list', views.VideoList.as_view(), name='video_list'),
    path('video_info', views.VideoInfo.as_view(), name='video_info'),
    path('watching/<int:vid>', views.video_count, name='counts'),
    path('join', views.signup, name='join'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('account', include('django.contrib.auth.urls')),
]
