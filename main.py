import os  # Github USERNAME, PASSWORD secret
import random  # Used to choose a random pic for post and song for reel
from time import sleep # Bypass bot detection from IG

# Import instagrapi - 3rd part IG API
from instagrapi import Client

# Import music utilities from song_utils.py module
import song_utils


# Login to client
cl = Client()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def Login():
    print("Logging in...")
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


# Upload a reel (with original audio)
reels = ["assets/reel_vids/car_reel.mp4", "assets/reel_vids/zuck_reel.mp4"]
random_reel_path = random.choice(reels)
thumbnail_path = "assets/thumbnail.jpg"


# usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
# location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
def Upload_Reel():
    print("Uploading normal reel...")
    cl.clip_upload(random_reel_path, caption, thumbnail_path)


# Upload a reel with music
def Upload_Reel_Music():
    print("Uploading reel with music...")
    try:
        song_tools = song_utils.SongUtils(cl)  # Initialize song_utils with instagrapi
        if random_reel_path == "assets/reel_vids/zuck_reel.mp4":
            track_metadata = song_tools.get_music("Candy Shop - 50 Cent")
            track_metadata.highlight_start_times_in_ms = [3925]
            cl.clip_upload_as_reel_with_music(random_reel_path, caption, track_metadata)
        else:
            ran_song = song_utils.random_song
            # See the name of song if causing an issue
            print(f"\n==============================\n{ran_song}\n==============================\n")
            track_metadata = song_tools.get_music(ran_song)
            if track_metadata == []:
                print(f"Could not find track for {ran_song}")
            cl.clip_upload_as_reel_with_music(random_reel_path, caption, track_metadata)
    except:
        print("Failed to upload reel with music, uploading normal reel instead...")
        Upload_Reel()

def ran_sleep():
    print("\n~~~~~ Sleeping for a random amount of time ~~~~~\n")
    return sleep(random.uniform(11, 37))

# Control functions to be run on IG Posting
def Run_IG_Posting():
    print("Running bot to post on Instagram...")
    Login()
    ran_sleep()
    Upload_Photo()
    ran_sleep()
    Upload_Reel_Music()
    print("Done.")

# Find metadata for a song
def Search_Music(song_to_search):
    print(f"Seaching music metadata for {song_to_search}")
    Login()
    #song_to_search = ""
    print(cl.search_music(song_to_search))


def main():
    Run_IG_Posting()
    # Search_Music("") # <--- Put song here

if __name__ == "__main__":
    main()
