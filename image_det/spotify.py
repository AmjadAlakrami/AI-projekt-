from spotify_local import SpotifyLocal

with SpotifyLocal() as s:
    s.connect("https://open.spotify.com/playlist/2B4z1NlkxuY7YWBlYupql7")
    