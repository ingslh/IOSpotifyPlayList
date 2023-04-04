from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from imdata import ImData


load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

print(client_id, client_secret)

def rep(s):
    li = []
    for i in s:
        li.append(i)
    for i in range(len(li)):
        if li[i] == ' ':
            li[i] = '%20'
    return ''.join(li)

def get_token():
  auth_string = client_id + ":" + client_secret
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Content-Type"  : "application/x-www-form-urlencoded"
  }
  data = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret
  print(data)
  result = post(url, headers = headers, data = data)
  json_result = json.loads(result.content)
  token = json_result["access_token"]
  return token

def get_auth_header(token):
  return {"Authorization": "Bearer  " + token}

def search_for_track(token, track_name, artist_name):
  url =  "https://api.spotify.com/v1/search"
  headers = get_auth_header(token)
  pre_query = f"q=remaster track:{track_name} artist:{artist_name}&type=track&limit=1"
  #pre_query = f"?q={track_name}&type:track"
  query = rep(pre_query)
  query_url = url + "?" +  query 
  result = get(query_url, headers = headers)
  json_result = json.loads(result.content)
  print(json_result)

def creat_sp():
  scope = "playlist-modify-public"
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
  return sp

#need to return playlist uri
def create_a_playlist(sp, playlist_name):
  user_id = sp.me()['id']
  ret = sp.user_playlist_create(user_id, playlist_name)
  return ret

def add_items_to_playlist(sp, playlist_uri, track_uris):
  sp.playlist_add_items(playlist_uri, track_uris)

def main():
  tracks_info = ImData.read_imdata()
  sp = creat_sp()
  playlist_name = "test1"
  result = create_a_playlist(sp, playlist_name)
  playlist_id = json_result = json.loads(result.content)

  token = get_token()
  search_for_track(token, "Doxy", "Miles Davis")

  for track in tracks_info:
    ret = search_for_track(token, track["track_name"], track["artist_name"])
    add_items_to_playlist(playlist_id, )

if __name__ == '__main__':
  main()
