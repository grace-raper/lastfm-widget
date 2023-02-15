import requests
import os
import sys


def lastfm_request(payload):
    headers = {'user-agent': os.getenv('LASTFM_USER')}
    payload['api_key'] = os.getenv('LASTFM_API_KEY')
    payload['format'] = 'json'
    payload['user'] = os.getenv('LASTFM_USER')
    response = requests.get('https://ws.audioscrobbler.com/2.0/',
                            headers=headers, params=payload)
    return response


def get_weekly_album_chart():
    payload = {'method': 'user.getweeklyalbumchart'}
    data = lastfm_request(payload).json()['weeklyalbumchart']['album']
    print(lastfm_request(payload).json())
    artist_and_album = []
    for i in range(len(data)):
        artist_and_album.append([data[i]['artist']['#text'],
                                 data[i]['name']])
    print(artist_and_album)
    return artist_and_album


def get_weekly_artist_chart(limit):
    print(limit)
    payload = {'method': 'user.getTopArtists', 'period': '7day', 'limit': limit}
    data = lastfm_request(payload).json()['topartists']['artist']
    top_artists = []
    for i in range(len(data)):
        top_artists.append([data[i]['name'],
                            data[i]['playcount'],
                            data[i]['url']])
    return top_artists


def get_weekly_track_chart(limit):
    print(limit)
    payload = {'method': 'user.getTopTracks', 'period': '7day', 'limit': limit}
    data = lastfm_request(payload).json()['toptracks']['track']
    top_tracks = []
    for i in range(len(data)):
        top_tracks.append([data[i]['artist']['name'],
                           data[i]['name'],
                           data[i]['playcount'],
                           data[i]['url']])
    return top_tracks


def update_readme_top_artists(artists):
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    lastfm_line_index = readme.index('<!-- LASTFM-TOP-ARTIST:START -->\n')
    for rank, artist in enumerate(artists):
        lastfm_line = str(rank + 1) + '. [' + artist[0] + '](' + artist[2] + ") - listened to " + str(
            artist[1]) + " times this week\n"
        lastfm_line_index += 1
        #print(str(rank) + " " + str(lastfm_line_index))
        readme[lastfm_line_index] = lastfm_line

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)


def update_readme_top_track(tracks):
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    lastfm_line_index = readme.index('<!-- LASTFM-TOP-TRACK:START -->\n')
    for track in tracks:
        lastfm_line = '* [' + track[1] + '](' + track[3] + ') - ' + track[0] + ' (' + str(
            track[2]) + " plays in the last 30 days)\n"
        lastfm_line_index += 1
        readme[lastfm_line_index] = lastfm_line

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)

#artist = get_weekly_artist_chart(5)
artist = get_weekly_artist_chart(os.getenv('ARTIST_COUNT'))
update_readme_top_artists(artist)

#tracks = get_weekly_track_chart(1)
tracks = get_weekly_track_chart(os.getenv('SONG_COUNT'))
update_readme_top_track(tracks)
