from django.shortcuts import render
from django.views import generic
#
from .models import Contents

class IndexView(generic.ListView):
    template_name = 'relocations/video_list.html'
    context_object_name = 'contents_list'

    def get_queryset(self):
        return Contents.objects.values_list('content_name', flat=True)
