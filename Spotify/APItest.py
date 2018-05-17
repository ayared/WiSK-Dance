# Test environment for querying Spotify API
import spotipy
import ReadToken
import webbrowser

# Get API token for Spotify interactions
token = ReadToken.GetToken('SpotifyToken.txt')
spotify = spotipy.Spotify(auth=token)

# Prompt user for search query
prompt = input('Search for a song: ')
# pass search string to Spotify, only returning track objects
results = spotify.search(prompt,type='track')

# Display results to user in format of 
# track #: [track name] by [artist name]
for index, item in enumerate(results['tracks']['items']):
     print('track ' + str(index) + ': ' + str(item['name']) + ' by ' + str(item['artists'][0]['name']))
print('Or enter CANCEL')
song_number = input('Select a song number: ')

# Pull user selection and open in Spotify Web Player
# Allows for user to not select a song and exit
if(song_number.isdigit()):
    song_number = int(song_number)
    url = results['tracks']['items'][song_number]['external_urls']['spotify']
    webbrowser.open(url)
else:
    print('Goodbye')
