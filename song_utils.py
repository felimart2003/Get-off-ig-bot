import random

class SongUtils:
    
    # List of songs
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

    @staticmethod
    def get_random_song():
        return random.choice(SongUtils.song_names)
    
    def __init__(self, client):
        self.client = client

    # Returns song metadata to use in Reels given a Str with the name and artist of song
    def get_music(self, song_title):
        print("Getting music for reel...")
        song_metadata = self.client.search_music(song_title)[0]
        return song_metadata

random_song = SongUtils.get_random_song()