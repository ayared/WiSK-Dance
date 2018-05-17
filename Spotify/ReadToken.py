# Read Spotify token information from local text file.
#Expects a filename string, in the current folder
#Returns the three lines in the file.
#File must be in the order of:
#CLIENT_ID
#CLIENT_SECRET
#REDIRECT_URI

import spotipy.util as util

# Pulls information assinged to WiSK-Dance by Spotify API
# from a local text file
def ReadFile(fileName): 
    f = open(fileName)
    tokens = f.read().splitlines()
    f.close()
    CLIENT_ID = tokens[0]
    CLIENT_SECRET = tokens[1]
    REDIRECT_URI = tokens[2]
    return CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def unitTest():
    a, b, c = ReadFile('SpotifyToken.txt')
    print(a)
    print(b)
    print(c)
    return

# Assembles Spotify API token from local file credentials
def GetToken(fileName):
    scope = 'user-library-read'
    username = 'WiSK-Dance'
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI = ReadFile(fileName)
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI)
    return token

# Redirect URL given by Spotify after successful execution of this code:
# https://example.com/callback/?code=AQCQaOt_4YgiUcK1i7ijXXo1-leHsG8TMnAo1w-9loBT0d52jDprYN1kNp7XJ4f69nJK4PpGCSV0oO1GEg3DjUcm8ipBaURFMyd3ZA2Y4-epTNf9duw1MlffitFV41mamn-6JEKdHLwl069z9ly__wb3rYoNFv-QLQZJi6ibgGO9zYzxn7StU3dpT86Dr0T4gyYcdcy5yK6l2CViI11qlt_bIQ7_Fg
