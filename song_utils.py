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
        "Still - Yung Lean, Bladee",
        "Fall Back - Lithe",
        "Cut - Duskus",
        "Still - Yung Lean, Bladee",
        "Pray 4 Me - Slimesito, Trippie Redd",
        "Ceremony - Skrillex, Yung Lean, Bladee",
        "Wings - Shoreline Mafia",
        "Hot Girl - OHGEESY",
        "bellyache - Billie Eilish",
        "Stash - Casper TNG, 6ixbuzz",
        "TRANCE - Dro Kenji",
        "RENOUND - Dro Kenji",
        "5% TINT - Travis Scott",
        "Stuck in a Dream - Pardyalone",
        "trix - whiterosemoxie",
        "beauty - mgk, Trippie Redd",
        "Motley Crew - Post Malone",
        "THE LINE (feat. d4vd) - The Kid LAROI, d4vd",
        "T.D (Lil Yachty & Tierra Whack feat. A$AP Rocky & Tyler, The Creator) - Lil Yachty, Tierra Whack, A$AP Rocky, Tyler, The Creator",
        "Missles (feat. Trippie Redd) - Lil Gnar, Trippie Redd",
        "Weeeeee - Trippie Redd",
        "3 Nights - Dominic Fike",
        "Phone Numbers - Dominic Fike, Kenny Beats",
        "Mob Ties - Drake",
        "Moonwalking in Calabasas (feat. Blueface) - Remix - DDG, Blueface",
        "Invincible - Pop Smoke",
        "Costa Rica - Bankrol Hayden",
        "Alpha - Guapdad 4000",
        "Dubai Shit - Huncho Jack, Travis Scott",
        "All the Smoke - Tyla Yaweh",
        "jack money bean - bbno$, Yung Gravy, lentra",
        "Red Room - Offset",
        "MAFIA - Travis Scott",
        "Falling Out of Love (feat. CashBently) - 909memphis, Cash Bently",
        "Hero - Tom The Mail Man",
        "Adding - Yung Fazo, SoFaygo",
        "Hit My Dance - Mills",
        "Vroom Vroom - Logic, C Dot Castro, halfBREED",
        "PINK FLOYD - JADY'S BIRTHDAY"
    ]

    @staticmethod
    def get_random_song():
        return random.choice(SongUtils.song_names)
    
    def __init__(self, client):
        self.client = client

    def get_music_metadata(self, song_to_search):
        print("Searching music...")
        # song_to_search = ""
        song_metadata_info = self.client.search_music(song_to_search)
        print(song_metadata_info)
        return song_metadata_info

    # Returns song metadata to use in Reels given a Str with the name and artist of song
    def get_music(self, song_title):
        print("Getting music for reel...")
        song_metadata = self.client.search_music(song_title)[0]
        return song_metadata

random_song = SongUtils.get_random_song()