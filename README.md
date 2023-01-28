**MET CS622 Final Project Description (20 points)**

You need to build a web crawler that download videos from a given link on video platform (youtube, Instagram and Tiktok) and given keywords. Then, trim the video and keep the important content of the video and discard the rest of the video.

This project I mainly used the Python Flask to developing web applications using python, implemented on Werkzeug and Jinja2. 

## Flask Set up

`__init__.py` is for set up the entire flask module. It contains CreateApp(). With init class, we can directly call the web page. Or we can create another `main.py` to run the web application. I also have this one and it works same as we call the app from init.py

## Youtube Section

	### Home page

By using YouTube Official API to search the videos. 

Seaching parameters, request from html, seperate vedio parameters, show them up in html with open source css format on web. 

### Download

Youtube Download is using the package `pytube` and provide yours session and headers to convert the youtube videos to download. It contains 4 html files, `home.html` is for input, `download.html` is for connecting to pytube and download the video, `error.html` is for the error code once your link is invalid, it shows that page, and last `layout.html` is the layout of the page it contains out sourced JavaScript and reference is from Miguel Fernandes. 

## TikTok

### Search and download

Reference: https://ssstik.io/en. 

Method: Used package selenium and beautifulsoup. Cookie and headers are automatically generated from TikTok.com's crul code. Making requests to ssstik.io and parse the data by using beautifulsoup. 

Call the method: Input the name you want to search, call the method, sleep for 1 sec. There is another difficulty on how to scroll the page, because normally it only shows 10 videos on pages, you want to find more then you need to scroll down the page. So, we have the while true loop to scroll the page to the bottom. Then final all html codes by using bs4. 

### Show

`tiktokshow.html` shows the result.

## Clips

`clips.py` is the file to segment the videos. Followed the instruction. 

## Instagram 

`insta.py` is for download the Instagram Reels, everything goes well before, both headers and session id, but it does not work recently, and I don't know why. 

Package used: instascrape. 