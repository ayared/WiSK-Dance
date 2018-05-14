# Test environment for querying Spotify API
import spotipy
import ReadToken
import webbrowser
token = ReadToken.GetToken('SpotifyToken.txt')
spotify = spotipy.Spotify(auth=token)

# Pulled from Spotify search
# j5_uri = 'spotify:artist:6wFId9Jhuf9AKVzWboOj2B' 
# results = spotify.artist_top_tracks(j5_uri)
prompt = input('Search for a song: ')
results = spotify.search(prompt,type='track')

for index, item in enumerate(results['tracks']['items']):
     print('track ' + str(index) + ': ' + str(item['name']))

song_number = int(input('Select a song number: '))
url = results['tracks']['items'][song_number]['external_urls']['spotify']

# print(results['tracks']['items'][2])
# url = results['tracks']['items'][2]['external_urls']['spotify']

webbrowser.open(url)
