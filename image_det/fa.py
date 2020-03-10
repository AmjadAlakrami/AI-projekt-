import os, spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

SPOTIPY_CLIENT_ID='830e5bf515504d4293f128fe0fa77191'
SPOTIPY_CLIENT_SECRET='abd8c43c229342dbbfff672a04f6d132'
SPOTIPY_REDIRECT_URI='https://www.google.com/'

username ="wj4xvcjslfruo3tv9wl1nq0rw"
try:
    token = util.prompt_for_user_token(username=username, scope="user-modify-playback-state", client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)
except:
    os.remove(".cache-"+username)
    token = util.prompt_for_user_token(username=username, scope="user-modify-playback-state", client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)

spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.previous_track()




# user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

# .next_track(device_id="642dd0908920b2c509a343176427f11618d69393")