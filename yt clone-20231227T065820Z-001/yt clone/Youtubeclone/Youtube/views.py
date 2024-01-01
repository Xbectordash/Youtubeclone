from django.shortcuts import render
from django.http import response
from .models import yt_attribute


# Create your views here.
def yt(request):

    video = yt_attribute.objects.all()

    return render(request, 'youtube.html', {'video': video})












# one thing you have to learn how to use jinger into jinger
    # yt = yt_attribute()
    # yt.Thumbnail='mkbhd.jpg'
    # yt.video_time='12:33'
    # yt.channel_pic='mkbhd.jpg'
    # yt.video_title='ios 17 Hands-On: Top 5 Features! 4'
    # yt.channel_name='Marques Brownlee 4'
    # yt.views= 3
    # yt.days= 2
    #
    # yt1 = yt_attribute()
    # yt1.Thumbnail='mkbhd.jpg'
    # yt1.video_time='12:33'
    # yt1.channel_pic='mkbhd.jpg'
    # yt1.video_title='ios 17 Hands-On: Top 5 Features! 3'
    # yt1.channel_name='Marques Brownlee 3'
    # yt1.views= 3
    # yt1.days= 2
    #
    # yt2 = yt_attribute()
    # yt2.Thumbnail='weeknd.jpg'
    # yt2.video_time='12:33'
    # yt2.channel_pic='weeknd.jpg'
    # yt2.video_title='ios 17 Hands-On: Top 5 Features! 2'
    # yt2.channel_name='Marques Brownlee 2'
    # yt2.views= 3
    # yt2.days= 2
    #
    # video = [yt,yt1,yt2]
