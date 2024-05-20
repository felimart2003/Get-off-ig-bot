# Import instagrapi
from instagrapi import Client
from instagrapi.types import Track # Music for reel

# Importing credentials of IG account from file
with open("credentials.txt", "r") as f:
  lines = f.read().splitlines()
  USERNAME = lines[0]
  PASSWORD = lines[1]

cl = Client()

#--------------------POST PIC--------------------

cl.login(USERNAME, PASSWORD)
photo_path = 'assets/postpic.png'
caption = 'Hello fellas, it\'s time to get off of Instagram!'

# Upload photo
#cl.photo_upload(photo_path, caption)

#--------------------REELS--------------------

reel_path = 'assets/reelvid.mp4'
thumbnail_path = 'assets/thumbnail.jpg'
#usertags = [Usertag(user=USERNAME, x=0.1, y=0.1)]
#location = Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)


# Upload a reel
#cl.clip_upload(reel_path, caption, thumbnail_path)

# Find track
#tracks = cl.search_music("Murder Sh!t - Bigbabygucci")
#print(tracks)


# Murder Sh!t by BIGBABYGUCCI
#Default start time is 40500
Murder = Track(
    id='1036137664247008',
    title='Murder Sh!t',
    subtitle='',
    display_artist='BIGBABYGUCCI',
    audio_cluster_id=1789929351434225,
    artist_id=None,
    cover_artwork_uri='https://cdn.fbsbx.com/v/t65.14500-21/399617650_713225400853358_1029519542890183627_n.jpg?stp=dst-jpg_p526x296&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=tbJ1LoyNIScQ7kNvgF3T5wA&_nc_ht=cdn.fbsbx.com&oh=00_AYDg_gUKcD92Eqjr0yP1KZw39Ajv20EhY61M41kzWVMliA&oe=664CD2A5',
    cover_artwork_thumbnail_uri='https://cdn.fbsbx.com/v/t65.14500-21/399617650_713225400853358_1029519542890183627_n.jpg?stp=dst-jpg_s168x128&_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_ohc=tbJ1LoyNIScQ7kNvgF3T5wA&_nc_ht=cdn.fbsbx.com&oh=00_AYBFfA34HVZPbYngvZmXlFHS3dRGU1nRE3sCQhZea7qrnQ&oe=664CD2A5',
    progressive_download_url='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/400261214_1268351050520732_5230517133119459928_n.mp4?_nc_cat=100&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=OEtHKMttCcYQ7kNvgFVd7Vx&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYBsKM08zpcp2MauZWPIxiYvM8rZ_KdA68s0AJxYqzP27g&oe=6650A459',
    fast_start_progressive_download_url='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/400261214_1268351050520732_5230517133119459928_n.mp4?_nc_cat=100&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=OEtHKMttCcYQ7kNvgFVd7Vx&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYBsKM08zpcp2MauZWPIxiYvM8rZ_KdA68s0AJxYqzP27g&oe=6650A459',
    reactive_audio_download_url=None,
    highlight_start_times_in_ms=[0],
    is_explicit=True,
    dash_manifest='<?xml version="1.0"?>\n<!-- MPD file Generated with GPAC version 0.7.2-DEV-revUNKNOWN_REV  at 2023-11-10T19:10:36.430Z-->\n<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M48.971S" maxSegmentDuration="PT0H0M2.005S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011,http://dashif.org/guidelines/dash264">\n <ProgramInformation moreInformationURL="http://gpac.io">\n  <Title>/work/audio_mpd.mpd generated by GPAC</Title>\n </ProgramInformation>\n\n <Period duration="PT0H1M48.971S">\n  <AdaptationSet segmentAlignment="true" lang="und" subsegmentAlignment="true" subsegmentStartsWithSAP="1">\n   <Representation id="1" mimeType="audio/mp4" codecs="mp4a.40.2" audioSamplingRate="48000" startWithSAP="1" bandwidth="130146">\n    <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>\n    <BaseURL>https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/400764582_677558057804451_185361165026731722_n.mp4?_nc_cat=111&amp;ccb=1-7&amp;_nc_sid=c2de2f&amp;_nc_ohc=hwzrd-Q4Pi4Q7kNvgEJzwS9&amp;_nc_ht=scontent-yyz1-1.cdninstagram.com&amp;oh=00_AYDKvl9n4jK5BXt6rlsPi7iMrgicDI_ZgoAgcWJJvh8Lmw&amp;oe=6650AA40</BaseURL>\n    <SegmentBase indexRangeExact="true" indexRange="801-1492">\n      <Initialization range="0-800"/>\n    </SegmentBase>\n   </Representation>\n  </AdaptationSet>\n </Period>\n</MPD>\n',
    uri='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/400764582_677558057804451_185361165026731722_n.mp4?_nc_cat=111&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=hwzrd-Q4Pi4Q7kNvgEJzwS9&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYDKvl9n4jK5BXt6rlsPi7iMrgicDI_ZgoAgcWJJvh8Lmw&oe=6650AA40',
    has_lyrics=True,
    audio_asset_id=1036137664247008,
    duration_in_ms=108970,
    dark_message=None,
    allows_saving=True,
    territory_validity_periods={}
    )

# Rokstarr by Dro Kenji
Rokstarr = Track(
    id='399677239664789',
    title='Rokstarr',
    subtitle='',
    display_artist='Dro Kenji',
    audio_cluster_id=958853779094574,
    artist_id=None,
    cover_artwork_uri='https://cdn.fbsbx.com/v/t65.14500-21/433829402_951537126208580_881465125632618041_n.png?stp=dst-webp_p526x296&_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=cDn4T5NDgNYQ7kNvgEWe0Ef&_nc_ht=cdn.fbsbx.com&oh=00_AYDnZ3xhvU90pQ8HYBfF8mOUdfRvu4WL_CClFMR2Qnx7XQ&oe=664CFFB9',
    cover_artwork_thumbnail_uri='https://cdn.fbsbx.com/v/t65.14500-21/433829402_951537126208580_881465125632618041_n.png?stp=dst-webp_s168x128&_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=cDn4T5NDgNYQ7kNvgEWe0Ef&_nc_ht=cdn.fbsbx.com&oh=00_AYAvff4rr8D6r5-OJQ7Vnugo7UroRhS9IXVMMLTCkgVwQw&oe=664CFFB9',
    progressive_download_url='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/435099157_435051089077458_4895965842638988814_n.mp4?_nc_cat=107&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=RllBqOaUW7cQ7kNvgGIIpmB&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYCF2lBwJ2SKwYul9tcTm-QN5hYpmL9ofkzRufMjThGq-A&oe=6650C8AA',
    fast_start_progressive_download_url='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/435099157_435051089077458_4895965842638988814_n.mp4?_nc_cat=107&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=RllBqOaUW7cQ7kNvgGIIpmB&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYCF2lBwJ2SKwYul9tcTm-QN5hYpmL9ofkzRufMjThGq-A&oe=6650C8AA',
    reactive_audio_download_url=None,
    highlight_start_times_in_ms=[16500,
    105000],
    is_explicit=True,
    dash_manifest='<?xml version="1.0"?>\n<!-- MPD file Generated with GPAC version 0.7.2-DEV-revUNKNOWN_REV  at 2024-04-10T21:14:07.671Z-->\n<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H2M51.050S" maxSegmentDuration="PT0H0M2.005S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011,http://dashif.org/guidelines/dash264">\n <ProgramInformation moreInformationURL="http://gpac.io">\n  <Title>/work/audio_mpd.mpd generated by GPAC</Title>\n </ProgramInformation>\n\n <Period duration="PT0H2M51.050S">\n  <AdaptationSet segmentAlignment="true" lang="und" subsegmentAlignment="true" subsegmentStartsWithSAP="1">\n <Representation id="1" mimeType="audio/mp4" codecs="mp4a.40.2" audioSamplingRate="48000" startWithSAP="1" bandwidth="130111">\n    <AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/>\n    <BaseURL>https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/436254928_825542122741805_7759305339269985226_n.mp4?_nc_cat=110&amp;ccb=1-7&amp;_nc_sid=c2de2f&amp;_nc_ohc=fF4yi6PX2C8Q7kNvgF1aX80&amp;_nc_ht=scontent-yyz1-1.cdninstagram.com&amp;oh=00_AYC74Yx3RhjdK-71SPlaDLSq5nBF16VdvB3TyZjfHWQcXQ&amp;oe=6650F035</BaseURL>\n    <SegmentBase indexRangeExact="true" indexRange="801-1864">\n      <Initialization range="0-800"/>\n    </SegmentBase>\n   </Representation>\n  </AdaptationSet>\n </Period>\n</MPD>\n',
    uri='https://scontent-yyz1-1.cdninstagram.com/v/t39.12897-6/436254928_825542122741805_7759305339269985226_n.mp4?_nc_cat=110&ccb=1-7&_nc_sid=c2de2f&_nc_ohc=fF4yi6PX2C8Q7kNvgF1aX80&_nc_ht=scontent-yyz1-1.cdninstagram.com&oh=00_AYC74Yx3RhjdK-71SPlaDLSq5nBF16VdvB3TyZjfHWQcXQ&oe=6650F035',
    has_lyrics=True,
    audio_asset_id=399677239664789,
    duration_in_ms=171049,
    dark_message=None,
    allows_saving=True,
    territory_validity_periods={})

# Find metadata for a song
#print(cl.search_music("Rokstarr - Dro Kenji"))

songs = [Murder, Rokstarr]

# Upload a reel with music
cl.clip_upload_as_reel_with_music(reel_path, caption, songs[1])