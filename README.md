# IOSpotifyPlayList

A script to migrate NetEase Cloud Music playlist to Spotify, base on [spotipy](https://github.com/spotipy-dev/spotipy) and [pyncm](https://github.com/mos9527/pyncm).

## How to Use

 1. Check if your Spotipy environment variable exists

    ### linux/macos
    ```shell
    echo $SPOTIPY_CLIENT_ID
    ```

    ### win
    ```shell
    #powershell
    $env:SPOTIPY_CLIENT_ID
    ```

    if not exist, need to add **SPOTIPY_CLIENT_ID** 、**SPOTIPY_CLIENT_SECRET** 、 **SPOTIPY_REDIRECT_URI** environment variable；

    Also you can fill your CLIENT_ID and CLIENT_SECRENT in *.env* file.

2. run script
    ```python
    python IOSpotifyPlayList.py -u "NetEase PlayList's url or id" (-m "new spotify playlist's name")

    #example 1
    python IOSpotifyPlayList.py -u "https://y.music.163.com/playlist?id=8270463198" -m "some cool staff"

    #example 2
    python IOSpotifyPlayList.py -u "8270463198"
    ```
    -u: (required) The URL or ID of a Netease playlist.

    -n: (Optional) Name of the newly created Spotify playlist, if not entered, today's date will be used as the playlist name.
