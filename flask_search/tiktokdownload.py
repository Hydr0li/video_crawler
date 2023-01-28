from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

# Reference: https://ssstik.io/en

def downloadVideo(link, id):
    cookies = {
        'ad_client': 'ssstik',
        '__cflb': '02DiuEcwseaiqqyPC5qr2kcTPpjPMVimuF8318hCovqkX',
        '_ga': 'GA1.2.1570876650.1671247575',
        '_gid': 'GA1.2.1171947177.1671247575',
        '__gads': 'ID=9b7e058518f96dda-22d29cc51dd9000b:T=1671247575:RT=1671247575:S=ALNI_MapR0u-tZTUkCqsbMitAia_OFf2gg',
        '__gpi': 'UID=000008d7039b3034:T=1671247575:RT=1671247575:S=ALNI_MZmhPCiRsPpL0E9Sg0l2RjIrqftUQ',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://ssstik.io/en',
        'HX-Request': 'true',
        'HX-Trigger': '_gcaptcha_pt',
        'HX-Target': 'target',
        'HX-Current-URL': 'https://ssstik.io/en',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://ssstik.io',
        'Alt-Used': 'ssstik.io',
        'Connection': 'keep-alive',
        # 'Cookie': 'ad_client=ssstik; __cflb=02DiuEcwseaiqqyPC5qr2kcTPpjPMVimuF8318hCovqkX; _ga=GA1.2.1570876650.1671247575; _gid=GA1.2.1171947177.1671247575; __gads=ID=9b7e058518f96dda-22d29cc51dd9000b:T=1671247575:RT=1671247575:S=ALNI_MapR0u-tZTUkCqsbMitAia_OFf2gg; __gpi=UID=000008d7039b3034:T=1671247575:RT=1671247575:S=ALNI_MZmhPCiRsPpL0E9Sg0l2RjIrqftUQ; _gat_UA-3524196-6=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'OEsycGY4',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]

    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"static/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

#input
username = input('Enter the user name of the TikToker you want to search:')
tiktokurl = "https://www.tiktok.com/@"
tiktokurl += username
driver = webdriver.Firefox()
# Change the tiktok link
driver.get(tiktokurl)

time.sleep(1)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

soup = BeautifulSoup(driver.page_source, "html.parser")
# this class may change, so make sure to inspect the page and find the correct class
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))
for index, video in enumerate(videos):
    downloadVideo(video.a["href"], index)
    time.sleep(10)