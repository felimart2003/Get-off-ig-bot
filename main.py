import os # Github USERNAME, PASSWORD secret
#from time import sleep
import random # Used to choose a random pic for post and song for reel

# Import instagrapi
from instagrapi import Client

# Import music tracks from tracks.py module
from tracks import *


# Login to client
cl = Client()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
def Login(): 
    cl.login(USERNAME, PASSWORD)

# Upload photo
photos = ['assets/post_pics/hugging.png', 'assets/post_pics/zuck_alien.png', 'assets/post_pics/zuck_portrait_dark.jpg', 'assets/post_pics/zuck_portrait_light.png']
random_photo_path = random.choice(photos) # Photo to be uploaded
caption = "Hello again fellas, it's time to get off Instagram. PROTIP: Like this post so the algorithm gives you more of these posts in the future. \nHASHTAGS: #getoffinstagram #addiction #fyp #foryou #explore #reels"
def Upload_Photo():
    cl.photo_upload(random_photo_path, caption)

# Upload a reel
reel_path = 'assets/reelvid.mp4'
thumbnail_path = 'assets/thumbnail.jpg'
#usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
#location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
def Upload_Reel():
    cl.clip_upload(reel_path, caption, thumbnail_path)

# Organize songs
songs = [Murder, Rokstarr, aisatsana]
# Generating random number to choose song for reel
random_song = random.choice(songs)

# Upload a reel with music
def Upload_Reel_Music():
    cl.clip_upload_as_reel_with_music(reel_path, caption, random_song)


#commenting out the sleeps to test if my account will get suspended again after I sucessfully appealed against my account suspension
# Control functions to be run
def Run_IG_Posting():
  Login()
#   sleep(10) 
  Upload_Photo()
#   sleep(10)
  Upload_Reel_Music()


# Find metadata for a song
def Search_Music(song_to_search):
    Login()
    #song_to_search = ""
    print(cl.search_music(song_to_search))


if __name__ == "__main__":
    Run_IG_Posting()

    # print("Seaching music...")
    # Search_Music('aisatsana [102] - Aphex Twin')
