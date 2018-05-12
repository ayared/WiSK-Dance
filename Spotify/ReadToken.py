# Read Spotify token information from local text file.
#Expects a filename string, in the current folder
#Returns the three lines in the file.
#File must be in the order of:
#CLIENT_ID
#CLIENT_SECRET
#REDIRECT_URI

def ReadToken(fileName): 
    f = open(fileName)
    tokens = f.read().splitlines()
    f.close()
    CLIENT_ID = tokens[0]
    CLIENT_SECRET = tokens[1]
    REDIRECT_URI = tokens[2]
    return CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def unitTest():
    a, b, c = ReadToken('SpotifyToken.txt')
    print(a)
    print(b)
    print(c)
