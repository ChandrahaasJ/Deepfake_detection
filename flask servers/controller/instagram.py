import instaloader
from instascrape import Reel
import time

# pip install instascrape

# This code will download the reel for sure, but not if you continue to make the request again and again, and hence, you need to pass the session id. Recently, due to updated policies of Instagram, it is not that easy to scrape it. Hence with the above code, we need to pass the session id into the headers as follows:

SESSIONID = "190b01404f1-8217ec"
# SessionID changes every time when you log out. Make sure that you provide the id at the time when you are logged in.

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}
#test@123
google_reel=Reel('https://www.instagram.com/reel/C8k5MzAyqXI/?utm_source=ig_web_copy_link')
google_reel.scrape(headers=headers)

# fstring Format = convenient way to embed python expressions inside string literals for formatting. 
google_reel.download(fp=f"D:/Projects/Deepfake_detection/Server/uploads.mp4")

print('Downloaded Successfully.')



# ig=instaloader.Instaloader()
# user=input("enter username")
# #ig.download_profile(user,profile_pic_only=True)
# post = instaloader.Post.from_shortcode(ig.context, "SHORTCODE")
# ig.download_post(post, target="TARGET_NAME")

