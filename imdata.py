
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
