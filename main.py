# Import instagrapi
from instagrapi import Client
from instagrapi.types import Track # Music for reel

# Importing credentials of IG account from file
import credentials.py

cl = Client()

cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
photo_path = 'assets/postpic.png'
caption = 'Hello fellas, it\'s time to get off of Instagram!'

# Upload photo
cl.photo_upload(photo_path, caption)

reel_path = 'assets/reelvid.mp4'
thumbnail_path = 'assets/thumbnail.jpg'

# Upload a reel
#cl.clip_upload(reel_path, caption, thumbnail_path)

track = Track(
    title='Murder Sh!t',
    artist='Bigbabygucci',
    uri='spotify:track:6BoQH9dk2kPg9iC2AgXF0Z'
    )
# Upload a reel with music
cl.clip_upload(reel_path, caption, thumbnail_path, track)