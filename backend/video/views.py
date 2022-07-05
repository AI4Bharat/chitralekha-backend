from io import StringIO
from datetime import timedelta

import requests
import webvtt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from .models import Video
from .serializers import VideoSerializer

# Define the YouTube Downloader object
ydl = YoutubeDL({'format': 'best'})


@api_view(['GET'])
def get_video(request):
    '''
    API Endpoint to get the direct URL to a video
    Endpoint: /video/
    Method: GET
    Query Params: video_url (required)
    '''

    # Get the video URL from the query params
    url = request.query_params.get('video_url')
    lang = request.query_params.get('lang', 'en')
    if url is None:
        return Response({
            'error': 'Video URL not provided in query params.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Get the video info from the YouTube API
    try:
        info = ydl.extract_info(url, download=False)
    except DownloadError:
        return Response({
            'error': f'{url} is an invalid video URL.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Extract required data from the video info
    normalized_url = info['webpage_url']
    title = info['title']
    duration = timedelta(seconds=info['duration'])

    # Create a new DB entry if URL does not exist, else return the existing entry
    video, created = Video.objects.get_or_create(
        url=normalized_url, defaults={'name': title, 'duration': duration})
    if created:
        video.save()

    # Return the Direct URL to the video
    direct_video_url = info['url']

    subtitles = None
    if 'subtitles' in info:
        if lang in info['subtitles']:
            # If it's named "English"
            subtitles = info['subtitles'][lang]
        else:
            # If it has a custom name like "English transcript by NPTEL"
            for s_key in info['subtitles']:
                if s_key.startswith(lang + '-'):
                    subtitles = info['subtitles'][s_key]
                    break

    # If manual captions not found, search for ASR transcripts
    if not subtitles and 'automatic_captions' in info:
        if lang in info['automatic_captions']:
            subtitles = info['automatic_captions'][lang]

    subtitles_list = []
    if subtitles:
        # Get the VTT URL from the subtitle info and make a GET request to fetch the data
        subtitle_url = [item['url'] for item in subtitles if item['ext'] == 'vtt'][0]
        subtitle_payload = requests.get(subtitle_url).text

        # Parse the VTT file contents and append to the subtitle list
        for caption in webvtt.read_buffer(StringIO(subtitle_payload)):
            subtitles_list.append({
                'start': caption.start,
                'end': caption.end,
                'text': caption.text
            })

    # Get the direct audio URL
    for fmt in info['formats']:
        if fmt['resolution'] == 'audio only' and fmt['ext'] == 'm4a' and fmt['quality'] == 3:
            direct_audio_url = fmt['url']
            break

    serializer = VideoSerializer(video)
    return Response({
        'direct_audio_url': direct_audio_url,
        'direct_video_url': direct_video_url,
        'subtitles': subtitles_list,
        'video': serializer.data
    }, status=status.HTTP_200_OK)


class VideoViewSet(ModelViewSet):
    '''
    API ViewSet for the Video model.
    Performs CRUD operations on the Video model.
    Endpoint: /video/api/
    Methods: GET, POST, PUT, DELETE
    '''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
