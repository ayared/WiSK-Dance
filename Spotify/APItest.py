# Test environment for querying Spotify API
import spotipy
import spotipy.util as util
import ReadToken

scope = 'user-library-read'
username = 'WiSK-Dance'

SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI = ReadToken.ReadToken('SpotifyToken.txt')
# Redirect URL given by Spotify after successful execution of this code:
# https://example.com/callback/?code=AQCQaOt_4YgiUcK1i7ijXXo1-leHsG8TMnAo1w-9loBT0d52jDprYN1kNp7XJ4f69nJK4PpGCSV0oO1GEg3DjUcm8ipBaURFMyd3ZA2Y4-epTNf9duw1MlffitFV41mamn-6JEKdHLwl069z9ly__wb3rYoNFv-QLQZJi6ibgGO9zYzxn7StU3dpT86Dr0T4gyYcdcy5yK6l2CViI11qlt_bIQ7_Fg
token = util.prompt_for_user_token(
    username,
    scope,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI)

spotify = spotipy.Spotify(auth=token)

# Pulled from Spotify search
j5_uri = 'spotify:artist:6wFId9Jhuf9AKVzWboOj2B' 
results = spotify.artist_top_tracks(j5_uri)

for track in results['tracks'][:10]:
    print('track: ' + track['name'])
