from flask import Blueprint, render_template, current_app, request, redirect, send_file, url_for, session
import requests
from isodate import parse_duration
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pytube import YouTube
from io import BytesIO
from scenedetect import SceneManager, VideoManager
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def index():
    # Use google APIs / google developer consolo
    # https://developers.google.com/youtube/v3/docs/search/list?hl=en_US
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    videos = []
    if request.method == 'POST':
        search_params = {
            'key' : current_app.config['YOUTUBE_API_KEY'],
            'q' : request.form.get('query'),
            'part' : 'snippet',
            'maxResults' : 9,
            'type' : 'video'
        }
        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []

        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.form.get('submit') == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')
        
        #print(video_ids)

        video_params = {
            'key' : current_app.config['YOUTUBE_API_KEY'],
            'id' : ','.join(video_ids),
            'part' : 'snippet,contentDetails',
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']
        video_ids = []
        for result in results:
            #print(result)
            video_data = {
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'duration' :  int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'title' : result['snippet']['title']
            }
            #print(video_data)
            videos.append(video_data)

    return render_template('index.html', videos=videos)

@main.route('/youtube', methods=['GET','POST'])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html", url = url)
    return render_template("home.html")

@main.route('/download', methods=['GET','POST'])
def download_video():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="Video - YT2Video.mp4", mimetype="video/mp4")
    return redirect(url_for("home"))


@main.route('/tiktokdownload', methods=['GET','POST'])
def downloadview():
    return render_template("tiktokshow.html")

@main.route('/clip', methods=['GET','POST'])
def find_scenes_save_video():
    if request.method == 'POST':
        if request.form.get('submit') == 'getclip':
            #first_name = request.form.get("fname")
            # Create our video & scene managers, then add the detector.
            video_path = request.form.get('clippath')

            video_manager = VideoManager([video_path])
            scene_manager = SceneManager()
            scene_manager.add_detector(ContentDetector())

            # Improve processing speed by downscaling before processing.
            video_manager.set_downscale_factor()

            # Start the video manager and perform the scene detection.
            video_manager.start()
            scene_manager.detect_scenes(frame_source=video_manager)

            # Save the video
            scene_list = scene_manager.get_scene_list()
            for index, scene in enumerate(scene_list):
                split_video_ffmpeg([video_path], [scene],
                                f"{index + 1}.mp4", "", suppress_output=True)
    
    return render_template("clip.html")
