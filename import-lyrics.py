import pandas as pd
import lyricsgenius
genius = lyricsgenius.Genius('XuHE9jmopg2A6eloIxsatHadE2qNu-Uy2MVqhLE3vGBwhDBaQTOGWKcQc4EHD3Kr')
artist = genius.search_artist("Phoebe Bridgers", max_songs= 3, sort = 'title')
print(artist.songs)

punisher = genius.search_albums("Punisher Phoebe Bridgers")
folklore_deluxe = genius.search_albums('folklore (deluxe version)', per_page= 20)
folklore = genius.search_albums('\u200bfolklore')
id_punisher = 573890
id_folklore_deluxe = 659926
id_folklore = 659925 ###669904 ## UGHHHHH 659926 deluxe edition

genius.album(id_punisher)
genius.album(id_folklore_deluxe)
punisher_tracks = genius.album_tracks(id_punisher)['tracks']
folklore_deluxe_tracks = genius.album_tracks(id_folklore_deluxe)['tracks']
folklore_tracks = genius.album_tracks(id_folklore)['tracks']

punisher_tracks[1]
punisher_tracks[1]['number']
punisher_tracks[1]['song']['title']
punisher_tracks[1]['song']['instrumental']
punisher_tracks[1]['song']['path']
punisher_tracks[1]['song']['id']
punisher_tracks[1]['song']['url']
punisher_tracks[1]['song']['stats']['pageviews']


folklore_tracks[1]
folklore_tracks[1]['number']
folklore_tracks[1]['song']['title']
folklore_tracks[1]['song']['instrumental']
folklore_tracks[1]['song']['path']
folklore_tracks[1]['song']['id']
folklore_tracks[1]['song']['url']
folklore_tracks[1]['song']['stats']['pageviews']


sample_song = genius.song(5044297)

sample_lyrics = genius.lyrics(punisher_tracks[1]['song']['url'])

keys = range(11)

sample_dict = {
    'artist': 'Phoebe Bridgers',
    'album': 'Punisher',
    'track_number': punisher_tracks[1]['number'],
    'track_title': punisher_tracks[1]['song']['title'],
    'instrumental': punisher_tracks[1]['song']['instrumental'],
    'track_path': punisher_tracks[1]['song']['path'],
    'track_id': punisher_tracks[1]['song']['id'],
    'track_url': punisher_tracks[1]['song']['url'],
    'track_pageviews': punisher_tracks[1]['song']['stats']['pageviews'],
    'track_lyrics': genius.lyrics(punisher_tracks[1]['song']['url'])
}

tuple_folklore = (
    'Taylor Swift',
    'folklore',
    folklore_tracks[1]['number'],
    folklore_tracks[1]['song']['title'],
    folklore_tracks[1]['song']['instrumental'],
    folklore_tracks[1]['song']['path'],
    folklore_tracks[1]['song']['id'],
    folklore_tracks[1]['song']['url'],
    folklore_tracks[1]['song']['stats']['pageviews'],
    genius.lyrics(folklore_tracks[1]['song']['url'])
)

tuple_punisher = (
    'Phoebe Bridgers',
    'Punisher',
    punisher_tracks[1]['number'],
    punisher_tracks[1]['song']['title'],
    punisher_tracks[1]['song']['instrumental'],
    punisher_tracks[1]['song']['path'],
    punisher_tracks[1]['song']['id'],
    punisher_tracks[1]['song']['url'],
    punisher_tracks[1]['song']['stats']['pageviews'],
    genius.lyrics(punisher_tracks[1]['song']['url'])
)


column_names = (
    "artist",
    "album",
    'track_number',
    'track_title',
    'instrumental',
    'track_path',
    'track_id',
    'track_url',
    'track_pageviews',
    'track_lyrics'
)

def with_tuples(loop_size=1e5):
    res = []

    for x in range(int(loop_size)):
        res.append((x-1, x, x+1))

    return pd.DataFrame(res, columns=("a", "b", "c"))


list_sample = []

list_sample.append(tuple_folklore)
list_sample.append(tuple_punisher)
df = pd.DataFrame(list_sample, columns=column_names)

# TODO function that gets the data I want in tuple form
# TODO function that loops throught tracks in album and uses previous function
