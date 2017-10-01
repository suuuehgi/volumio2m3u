# volumio2m3u
Generate [ext-m3u](https://de.wikipedia.org/wiki/M3U#Erweiterte_M3U) files from Volumio playlist format.

# Version
0.1

# Dependencies
* `python3 >= 3.1`

# Usage
`./volumio2m3u <filename.m3u>`

```
-c, --changelog
-h, --help
-v, --version
```

Custom playlists are located in:

* `/data/playlist` (custom playlists)
* `/data/favourites/my-web-radio` (*My Web Radios*)
* `/data/favourites/radio-favourites` (*Favorite Radios*)

# Assumptions

* Volumio playlists have `.volumio` extension
* Playlist items contain `http`, `https` or a file extension `.something`
    * If a file has no metadata, the base-filename will be taken

# Example Usage
```
$ ssh volumio@volumiocomputer "cat /data/favourites/my-web-radio" > /tmp/myplaylist.volumio
$ volumio2m3u /tmp/myplaylist.volumio > /tmp/myplaylist.m3u
```
