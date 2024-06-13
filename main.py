import os  # Github USERNAME, PASSWORD secret
import random  # Used to choose a random pic for post and song for reel

# Import instagrapi
from instagrapi import Client

# Import music tracks from tracks.py module
from tracks import *


# Login to client
cl = Client()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
def Login():
    cl.login(USERNAME, PASSWORD)


# Upload photo
photos = [
    "assets/post_pics/hugging.png",
    "assets/post_pics/zuck_alien.png",
    "assets/post_pics/zuck_portrait_dark.jpg",
    "assets/post_pics/zuck_portrait_light.png",
]
random_photo_path = random.choice(photos)  # Photo to be uploaded
# 414 chars
caption = "Hello fellas, it's time to get off Instagram.\nPROTIP: Like this post so the algorithm gives you more of these posts in the future.\n.\n.\n.\n#getoffig #addiction #fyp #explore #reels #andrewtate #samsulek #biden #trump #monkeybrain #dopamine #scrolling #stopscrolling #funny #cars #videogames #fortnite #rocketleague #leagueoflegends #lol #gta5 #gta6 #civ6 #minecraft #eveonline #taylorswift #kendricklamar #drake"
def Upload_Photo():
    print("Uploading photo...")
    cl.photo_upload(random_photo_path, caption)


# Upload a reel
reels = [
    "assets/reel_vids/car_reel.mp4",
    "assets/reel_vids/zuck_reel.mp4",
    "assets/reel_vids/motivation.mp4",
]
random_reel_path = random.choice(reels)
thumbnail_path = "assets/thumbnail.jpg"
# usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
# location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
def Upload_Reel():
    print("Uploading reel...")
    cl.clip_upload(random_reel_path, caption, thumbnail_path)


# Organize songs
# ADD: Still Yung lean, Pray 4 Me Slimesito
songs = [
    # Murder,
    # Rokstarr,
    # aisatsana,
    # Breathe,
    # ICE,
    # Pretty_Girls_Like_Anime,
    # Victorious,
    # THROW_UP,
    # Notes_From_A_Wrist,
    # All_I_Need,
    # Cities,
    # Let_Go,
    # Purple_Substance,
    Fall_Back
]
# Generating random number to choose song for reel
random_song = random.choice(songs)


# Upload a reel with music
def Upload_Reel_Music():
    try:
        print("Uploading reel with music...")
        if random_reel_path == "assets/reel_vids/zuck_reel.mp4":
            cl.clip_upload_as_reel_with_music(random_reel_path, caption, Candy_Shop)
        else:
            cl.clip_upload_as_reel_with_music(random_reel_path, caption, random_song)
    except:
        Upload_Reel()


# Control functions to be run
def Run_IG_Posting():
    print("Posting on Instagram...")
    Login()
    Upload_Photo()
    Upload_Reel_Music()
    print("Done.")


# Find metadata for a song
def Search_Music(song_to_search):
    print("Searching music...")
    Login()
    # song_to_search = ""
    print(cl.search_music(song_to_search))


def main():
    Run_IG_Posting()

    # Search_Music("fall back - lithe") # <--- Put song to search here


if __name__ == "__main__":
    main()
