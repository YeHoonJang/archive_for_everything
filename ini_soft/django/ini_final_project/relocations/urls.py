from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('video_list', views.VideoList.as_view(), name='video_list'),
    path('video_info', views.VideoInfo.as_view(), name='video_info'),
    path('watching/<int:vid>', views.video_count, name='counts'),
    path('join', views.signup, name='join'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload', views.upload_file, name='upload'),
    ]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
