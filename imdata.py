import pyncm, pyncm.apis


class ImData:

  @staticmethod
  def read_imdata():
    ret = []
    f = open("imdata.txt")
    lines = f.readlines()
    for line in lines:
        track_info = {}
        if line.count('-') == 1:
            track_name, artist_name = line.split('-', 1)
            artist_name = artist_name.strip()
            track_name = track_name.rstrip()
            track_info["track_name"] = track_name
            track_info["artist"] = artist_name
            ret.append(track_info)
        elif line.count('-') > 1:
            track_name, artist_name = line.rsplit('-', 1)
            artist_name = artist_name.strip()
            track_name = track_name.rstrip()
            track_info["track_name"] = track_name
            track_info["artist"] = artist_name
            ret.append(track_info)
        else: 
            continue
    return ret

  def cut(obj, sec):
    return [obj[i : i + sec] for i in range(0, len(obj), sec)]

  @staticmethod
  def ReadNetEasePlayList(id_or_url : str):
    ret = {}
    if id_or_url.isdigit():
      ret = pyncm.apis.playlist.GetPlaylistInfo(id_or_url)
    elif id_or_url.find("music.163.com") != -1:
      id_beg_pos = id_or_url.find("id=") + 3
      id_end_pos = id_or_url.find("id=") + 13
      playlist_id = id_or_url[id_beg_pos : id_end_pos]
      ret = pyncm.apis.playlist.GetPlaylistInfo(playlist_id)
    else : 
      return []

    trackids_info = ret["playlist"]["trackIds"]
    ids = []
    for trackid in trackids_info : 
      ids.append(trackid["id"])

    tracks = []
    if len(ids) < 1000:
      tracks = pyncm.apis.track.GetTrackDetail(ids)
    else:
      ids_list = cut(ids,1000)
      for tmp_ids in ids_list:
        tmp_tracks = pyncm.apis.track.GetTrackDetail(tmp_ids)
        tracks.append(tmp_tracks)
    return tracks
      
