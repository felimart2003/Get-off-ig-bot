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
        cl.clip_upload_as_reel_with_music(random_reel_path, caption, 'Candy_Shop')
    else:
        track_url = Get_Music()
        cl.clip_upload_as_reel_with_music(random_reel_path, caption, track_url)

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
    # Fetch the latest metadata for the song
    new_metadata = cl.search_music(song_title)[0]
    return new_metadata

class MusicMetadata:
    def __init__(self, id, title, subtitle, display_artist, audio_cluster_id, artist_id, cover_artwork_uri, cover_artwork_thumbnail_uri, progressive_download_url, fast_start_progressive_download_url, reactive_audio_download_url, highlight_start_times_in_ms, is_explicit, dash_manifest, uri, has_lyrics, audio_asset_id, duration_in_ms, dark_message, allows_saving, territory_validity_periods):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.display_artist = display_artist
        self.audio_cluster_id = audio_cluster_id
        self.artist_id = artist_id
        self.cover_artwork_uri = cover_artwork_uri
        self.cover_artwork_thumbnail_uri = cover_artwork_thumbnail_uri
        self.progressive_download_url = progressive_download_url
        self.fast_start_progressive_download_url = fast_start_progressive_download_url
        self.reactive_audio_download_url = reactive_audio_download_url
        self.highlight_start_times_in_ms = highlight_start_times_in_ms
        self.is_explicit = is_explicit
        self.dash_manifest = dash_manifest
        self.uri = uri
        self.has_lyrics = has_lyrics
        self.audio_asset_id = audio_asset_id
        self.duration_in_ms = duration_in_ms
        self.dark_message = dark_message
        self.allows_saving = allows_saving
        self.territory_validity_periods = territory_validity_periods

# Clean metadata from song so it can be used for instagrapi
def clean_metadata(metadata):
    # Extract URL from the Url object and other necessary fields
    cleaned_metadata = MusicMetadata(
        id=metadata.id,
        title=metadata.title,
        subtitle=metadata.subtitle,
        display_artist=metadata.display_artist,
        audio_cluster_id=metadata.audio_cluster_id,
        artist_id=metadata.artist_id,
        cover_artwork_uri=str(metadata.cover_artwork_uri) if metadata.cover_artwork_uri else None,
        cover_artwork_thumbnail_uri=str(metadata.cover_artwork_thumbnail_uri) if metadata.cover_artwork_thumbnail_uri else None,
        progressive_download_url=str(metadata.progressive_download_url) if metadata.progressive_download_url else None,
        fast_start_progressive_download_url=str(metadata.fast_start_progressive_download_url) if metadata.fast_start_progressive_download_url else None,
        reactive_audio_download_url=str(metadata.reactive_audio_download_url) if metadata.reactive_audio_download_url else None,
        highlight_start_times_in_ms=metadata.highlight_start_times_in_ms,
        is_explicit=metadata.is_explicit,
        dash_manifest=metadata.dash_manifest,
        uri=str(metadata.uri) if metadata.uri else None, # Convert Url object to string
        has_lyrics=metadata.has_lyrics,
        audio_asset_id=metadata.audio_asset_id,
        duration_in_ms=metadata.duration_in_ms,
        dark_message=metadata.dark_message,
        allows_saving=metadata.allows_saving,
        territory_validity_periods=metadata.territory_validity_periods
    )
    return cleaned_metadata

def Get_Music():
    print("Getting music for reel...")
    song_metadata = get_metadata(random_song_name)
    return clean_metadata(song_metadata)
# --------------------------------------------------

# Control functions to be run
def Run_IG_Posting():
    print("Running bot to post on Instagram...")
    Login()
    # Upload_Photo()
    # Get_Music()
    # random_song = Get_Music()
    Upload_Reel_Music()

def main():
    Run_IG_Posting()

if __name__ == "__main__":
    main()