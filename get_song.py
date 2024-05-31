import random
from instagrapi import Client

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

# Clean metadata from song so it can be used for instagrapi
def clean_metadata(metadata):
    metadata_str = str(metadata)
    metadata_str = metadata_str.replace("Url(", "").replace(")", "").replace("territory_validity_periods={}", "territory_validity_periods={})")
    # Revert metadata_str from str to object
    metadata_obj = eval(metadata_str)
    return metadata_obj

def Get_Music():
  print("Getting music for reel...")
  song_metadata = get_metadata(random_song_name)
  random_song = clean_metadata(song_metadata)