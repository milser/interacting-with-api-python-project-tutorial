import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()
spotipy.Spotify()

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
wombats_uri = 'spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

album_request = spotify.artist_albums(wombats_uri, album_type='album')
top_tracks_request = spotify.artist_top_tracks(wombats_uri)
albums = album_request['items']

#print(top_tracks_request)
track_data = []
for track in top_tracks_request['tracks'][:10]:
    print('Name: ' + track['name']+' - Popularity: '+str(track['popularity'])+' - Duracion: '+str(track['duration_ms']))
    track_dict = {
        'Name': track['name'],
        'Popularity': track['popularity'],
        'Duracion': track['duration_ms']
    }
    track_data.append(track_dict)
    
df = pd.DataFrame(track_data)

# Mostrar el DataFrame
print(df)


#Step 6
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Duracion', y='Popularity')
plt.title('Relationship Between Duration and Popularity')
plt.xlabel('Duration (ms)')
plt.ylabel('Popularity')
plt.show()

## As we can see there is no clear relation btween the duration and the popularity, two of the songs wiht the most 
# popularity has very different durations.
