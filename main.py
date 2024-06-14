import os # Github USERNAME, PASSWORD secret
import random # Used to choose a random pic for post and song for reel

# Import instagrapi
from instagrapi import Client

# Import music tracks from tracks.py module
# from tracks import *
# from get_song import Get_Music

# Login to client
cl = Client()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
def Login(): 
  print("Logging in...")
  cl.login(USERNAME, PASSWORD)

# Upload photo
photos = ['assets/post_pics/hugging.png', 'assets/post_pics/zuck_alien.png', 'assets/post_pics/zuck_portrait_dark.jpg', 'assets/post_pics/zuck_portrait_light.png']
random_photo_path = random.choice(photos) # Photo to be uploaded
# 414 chars
caption = "Hello fellas, it's time to get off Instagram.\nPROTIP: Like this post so the algorithm gives you more of these posts in the future.\n.\n.\n.\n#getoffig #addiction #fyp #explore #reels #andrewtate #samsulek #biden #trump #monkeybrain #dopamine #scrolling #stopscrolling #funny #cars #videogames #fortnite #rocketleague #leagueoflegends #lol #gta5 #gta6 #civ6 #minecraft #eveonline #taylorswift #kendricklamar #drake"
def Upload_Photo():
  print("Uploading photo...")
  cl.photo_upload(random_photo_path, caption)

# Upload a reel
reels = ['assets/reel_vids/car_reel.mp4', 'assets/reel_vids/zuck_reel.mp4']
random_reel_path = random.choice(reels)
thumbnail_path = 'assets/thumbnail.jpg'
# usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
# location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
def Upload_Reel():
  cl.clip_upload(random_reel_path, caption, thumbnail_path)

# Upload a reel with music
def Upload_Reel_Music():
  print("Uploading reel...")
  if random_reel_path == 'assets/reel_vids/zuck_reel.mp4':
    track_metadata = Get_Music("Candy Shop - 50 Cent")
    track_metadata.highlight_start_times_in_ms = [3500]
    cl.clip_upload_as_reel_with_music(random_reel_path, caption, track_metadata)
  else:
    track_metadata = Get_Music(random_song_name)
    cl.clip_upload_as_reel_with_music(random_reel_path, caption, track_metadata)

# --------------------------------------------------
# Organize songs
song_names = [
    "Murder Sh!t - BIGBABYGUCCI",
    "Rokstarr - Dro Kenji",
    "aisatsana[102] - Aphex Twin",
    "Breathe - Yeat",
    "ICEWHORE! - Lumi Athena",
    "Pretty Girls Like Anime - Kid J",
    "Victorious - Yung Lean, Bladee",
    "THROW UP - Dro Kenji",
    "Notes From A Wrist - d4vid",
    "All I Need - Slushii, Aviella",
    "Cities - Throttle",
    "Let Go - Duskus",
    "Purple Substance - lil obnoxious",
    "Cut - Duskus",
    "Still - Yung Lean, Bladee",
    "Pray 4 Me - Slimesito, Trippie Redd"
]
# Generating random number to choose song for reel
random_song_name = random.choice(song_names)

# Retrieve metadata for a song given a song name
def get_metadata(song_title):
    print("Retrieving metadata for " + song_title + "...")
    new_metadata = cl.search_music(song_title)[0]
    return new_metadata

def Get_Music(reel_song):
    print("Getting music for reel...")
    song_metadata = get_metadata(reel_song)
    return song_metadata
# --------------------------------------------------

# Control functions to be run
def Run_IG_Posting():
  print("Running bot to post on Instagram...")
  Login()
  Upload_Photo()
  Upload_Reel_Music()
  
def main():
    Run_IG_Posting()

if __name__ == "__main__":
  main()
