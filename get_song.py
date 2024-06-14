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
def get_metadata(cl, song_title):
    print("Retrieving metadata for " + song_title + "...")
    new_metadata = cl.search_music(song_title)[0]
    return new_metadata

def Get_Music(cl, reel_song):
    print("Getting music for reel...")
    song_metadata = get_metadata(cl, reel_song)
    return song_metadata