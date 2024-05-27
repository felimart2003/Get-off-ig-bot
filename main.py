import os # Github USERNAME, PASSWORD secret
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
#510 chars
caption = "Hello again fellas, it's time to get off Instagram.\nPROTIP: Like this post so the algorithm gives you more of these posts in the future.\n.\n.\n.\nHASHTAGS: #getoffinstagram #addiction #fyp #foryou #explore #reels #andrewtate #samsulek #biden #trump #monkey #monkeybrain #dopamine #scrolling #stopscrolling #coolvideo #funny #cars #videogames #fortnite #rocketleague #leagueoflegends #lol #gta5 #gta6 #civ6 #minecraft #eveonline #epicgames #taylorswift #lanadelrey #kendricklamar #drake #suffering #takeabreak"
def Upload_Photo():
    cl.photo_upload(random_photo_path, caption)

# Upload a reel
reels = ['assets/reel_vids/car_reel.mp4', 'assets/reel_vids/zuck_reel.mp4']
random_reel_path = random.choice(reels)
thumbnail_path = 'assets/thumbnail.jpg'
#usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
#location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
def Upload_Reel():
    cl.clip_upload(random_reel_path, caption, thumbnail_path)

# Organize songs
songs = [Murder, Rokstarr, aisatsana]
# Generating random number to choose song for reel
random_song = random.choice(songs)

# Upload a reel with music
def Upload_Reel_Music():
  if random_reel_path == 'assets/reel_vids/zuck.mp4':
    cl.clip_upload_as_reel_with_music(random_reel_path, caption, Candy_Shop)
  cl.clip_upload_as_reel_with_music(random_reel_path, caption, random_song)


#commenting out the sleeps to test if my account will get suspended again after I sucessfully appealed against my account suspension
# Control functions to be run
def Run_IG_Posting():
  print("Posting on Instagram...")
  Login()
  print("Logged in! Uploading photo...")
  Upload_Photo()
  print("Uploading reel...")
  Upload_Reel_Music()


# Find metadata for a song
def Search_Music(song_to_search):
    Login()
    #song_to_search = ""
    print(cl.search_music(song_to_search))


if __name__ == "__main__":
    Run_IG_Posting()

    #print("Seaching music...")
    #Search_Music('Candy Shop - 50 cent') # <--- Put song to search here
