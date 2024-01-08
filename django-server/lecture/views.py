from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Lecture, Video
from datetime import timedelta
# Create your views here.


def lecture(request, lecture_name):
    if request.method == "POST":
        lecture = Lecture.objects.get(id=request.POST['lecture_id'])
        videos = lecture.videos.all()

        context = {
            'lecture': lecture,
            'videos': videos,
            'video_count': len(videos)
        }
        return render(request, './lecture/index.html', context)


@require_http_methods(["POST"])
def save_playback(request):
    pass
