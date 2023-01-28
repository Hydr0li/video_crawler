from instascrape import Reel
import time

#pigeon_state	{"sequenceID":30,"lastEventTime":1671434724224,"sessionID":"1852941387a-76d945"}
SESSIONID = "{1852941387a-76d945}"
# SessionID changes every time when you log out. Make sure that you provide the id at the time when you are logged in.

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
"cookie":f'sessionid={SESSIONID};'
}
#test
google_reel=Reel("https://www.instagram.com/reel/CmLVB9zg0rn/?utm_source=ig_web_copy_link")
google_reel.scrape(headers=headers)

# fstring Format = convenient way to embed python expressions inside string literals for formatting. 
google_reel.download(fp=f"/Users/haizhouli/Documents/BU/Fall2022/CS622/Video_search/flask_search/static/{int(time.time())}.mp4")

print('Downloaded Successfully.')