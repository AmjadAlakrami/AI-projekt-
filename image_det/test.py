import json, cv2, os, spotipy, yolo, time, json
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
import spotipy.util as util

DEFAULT_CONFIG_FILE = os.path.join("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/image_det", "config.json")
DEFAULT_WEIGHT_FILE = os.path.join("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/image_det", "model.h5")

config_buffer = open(DEFAULT_CONFIG_FILE,'r') 
config = json.loads(config_buffer.read())

a = []
  
# 2. create yolo instance & predict
yolo = create_yolo(config['model']['architecture'],
                    config['model']['labels'],
                    config['model']['input_size'],
                    config['model']['anchors'])
yolo.load_weights(DEFAULT_WEIGHT_FILE)

def Create_token():
    if not config["spotify_config"]["Done"]:
        config["spotify_config"]["SPOTIPY_CLIENT_ID"] = input("Inter your spotipy client id: ")
        config["spotify_config"]["SPOTIPY_CLIENT_SECRET"] = input("Inter your spotipy client secret: ")
        config["spotify_config"]["SPOTIPY_REDIRECT_URI"] = input("Inter your spotipy redirect uri: ")
        config["spotify_config"]["USERNAME"] = input("Inter your spotify username: ")
        config["spotify_config"]["Done"] = True
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)

def Connect_to_token():
    token_1 = util.prompt_for_user_token(username=config["spotify_config"]["USERNAME"], scope=config["spotify_config"]["SCOPE"],client_id=config["spotify_config"]["SPOTIPY_CLIENT_ID"], redirect_uri=config["spotify_config"]["SPOTIPY_REDIRECT_URI"], client_secret=config["spotify_config"]["SPOTIPY_CLIENT_SECRET"])
    spotifyObject_1 = spotipy.Spotify(auth=token_1)
    return spotifyObject_1

def creat_list():
    for List in range(0,Connect_to_token().user_playlists(user=config["spotify_config"]["USERNAME"])["total"]):
        a.append(Connect_to_token().user_playlists(user=config["spotify_config"]["USERNAME"])["items"][List]["name"])
    if "my super cool AI playlist" not in a:
        Connect_to_token().user_playlist_create(user=config["spotify_config"]["USERNAME"], name="my super cool AI playlist", public=False, description="my super cool AI playlist made with my super cool AI program")
        config["spotify_config"]["list_created"] = Connect_to_token().user_playlists(user=config["spotify_config"]["USERNAME"])["items"][0]["id"]
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)
        print("created")

def Add_to_list():
    if Connect_to_token().currently_playing()["item"]["id"] not in config["spotify_config"]["track_in_list"]:
        config["spotify_config"]["track_in_list"].append(Connect_to_token().currently_playing()["item"]["id"])
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)
        Connect_to_token().user_playlist_add_tracks(user=config["spotify_config"]["USERNAME"] ,playlist_id=config["spotify_config"]["list_created"],tracks=[Connect_to_token().currently_playing()["item"]["id"]])
        print("added")      
    else:
        print("track is already in list")

def Change_song():
    for x in boxes:
        if x[0] > 150 :
            if x[0]-260 >= 140:
                Connect_to_token().next_track()
        if x[0] < 90 :
            if x[0]-260 < -275:
                Connect_to_token().previous_track()


cap = cv2.VideoCapture(0)
Create_token()
Connect_to_token()
creat_list()
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while True:
    boxes, probs = yolo.predict(frame1, config["model"]["DEFAULT_THRESHOLD"])

    labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
    # 4. save detection result
    frame1 = draw_scaled_boxes(frame1, boxes, probs, config['model']['labels'])
    label_list = config['model']['labels']
    cv2.imshow("imageo", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    cv2.waitKey(1)


    if 0 in labels:
        try:
            Add_to_list()
        except:
            input(" No active device found ... press ENTER when you are back on track")
    if 1 in labels:
        try:
            diff = cv2.absdiff(frame1, frame2)
            print(diff)
            Change_song()
        except:
            input(" No active device found ... press ENTER when you are back on track")

cv2.destroyAllWindows()
        