
from django.shortcuts import render
from pytube import YouTube

def index(request):
    try:
        if request.method == 'POST':
            try:
                link = request.POST['link']
                video = YouTube(link)
                stream = video.streams.get_lowest_resolution()
                video_title = video.title

                # Get the download URL of the video
                download_url = stream.url

                # Render HTML page with video download link
                return render(request, 'index.html', {'download_url': download_url, 'video_title': video_title})

            except Exception as e:
                return render(request, 'index.html', {'msg': 'Video not found'})

        return render(request, 'index.html', {'msg': ''})

    except Exception as e:
        return render(request, "index.html", {"msg": "Sorry, something went wrong!"})