from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from imdata import ImData
from urllib import request, parse
import os
import spotipy

def search_for_track(sp, track_name, artist_name):
  search_ret = sp.search(track_name, 10)
  search_tracks = search_ret["tracks"]["items"]
  for track in search_tracks:
    test_name  = track["name"]
    test_artist = track["artists"][0]["name"]
    if track["name"].lower() == track_name.lower() and track["artists"][0]["name"].lower() == artist_name.lower() :
       return True , track["uri"]

  return False, ""


def creat_sp():
  scope = "playlist-modify-public"
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
  return sp

#need to return playlist uri
def create_a_playlist(sp, playlist_name):
  user_id = sp.me()['id']
  ret = sp.user_playlist_create(user_id, playlist_name)
  return ret["id"]

def add_items_to_playlist(sp, playlist_uri, track_uris, position=None):
  plid = sp._get_id("playlist", playlist_uri)
  ftracks = [sp._get_uri("track", tid) for tid in [track_uris]]
  return sp._post(
         "playlists/%s/tracks" % (plid),
          payload=ftracks,
          position=position,
  )

def main():

  load_dotenv()

  client_id = os.getenv("SPOTIPY_CLIENT_ID")
  client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
  redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

  print(client_id, client_secret)

  tracks_info = ImData.read_imdata()
  sp = creat_sp()
  playlist_name = "test1"

  ser_id = sp.me()['id']
  playlist_id = create_a_playlist(sp, playlist_name)

  tracks_count = len(tracks_info)
  cnt = 0
  for track in tracks_info:
    ret,track_uri = search_for_track(sp, track["track_name"], track["artist"])
    if ret :
      response = add_items_to_playlist(sp, playlist_id, track_uri)
      if "snapshot_id" in response:
        cnt += 1
        print(f"Import to \"{playlist_id}\"({cnt} / {tracks_count}) : " + track["track_name"] + " - " + track["artist"])


if __name__ == '__main__':
  main()



