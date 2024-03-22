import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()
spotipy.Spotify()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
wombats_uri = 'spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

album_request = spotify.artist_albums(wombats_uri, album_type='album')
top_tracks_request = spotify.artist_top_tracks(wombats_uri)
albums = album_request['items']

#print(top_tracks_request)

for track in top_tracks_request['tracks'][:5]:
    print('Name: ' + track['name']+' - Popularity: '+str(track['popularity'])+' - Duracion: '+str(track['duration_ms']))