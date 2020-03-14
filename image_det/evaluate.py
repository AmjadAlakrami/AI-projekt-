import json, cv2, os, spotipy, yolo, time
import cv2
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
import spotipy.util as util

DEFAULT_CONFIG_FILE = os.path.join("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/image_det", "config.json")
DEFAULT_WEIGHT_FILE = os.path.join("C:/Users/amjad/Downloads", "model.h5")
DEFAULT_THRESHOLD = 0.55

SPOTIPY_CLIENT_ID='830e5bf515504d4293f128fe0fa77191'
SPOTIPY_CLIENT_SECRET='abd8c43c229342dbbfff672a04f6d132'
SPOTIPY_REDIRECT_URI='https://www.google.com/'
USERNAME ="wj4xvcjslfruo3tv9wl1nq0rw"
SCOPE = "user-modify-playback-state user-read-currently-playing playlist-modify-private"

if __name__ == '__main__':
    try:
        token_1 = util.prompt_for_user_token(username=USERNAME, scope=SCOPE,client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)
    except :

        token_1 = util.prompt_for_user_token(username=USERNAME, scope=SCOPE ,client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)
    spotifyObject_1 = spotipy.Spotify(auth=token_1)

    with open(DEFAULT_CONFIG_FILE) as config_buffer:
        config = json.loads(config_buffer.read())

    # 2. create yolo instance & predict
    yolo = create_yolo(config['model']['architecture'],
                       config['model']['labels'],
                       config['model']['input_size'],
                       config['model']['anchors'])
    yolo.load_weights(DEFAULT_WEIGHT_FILE )
    a = []
    # for i in range(0, spotifyObject_1.user_playlist_tracks(playlist_id="4QGhaoFzUW8m7qeBur7Kfi")["total"]-1):
    #     a.append(spotifyObject_1.user_playlist_tracks(playlist_id="4QGhaoFzUW8m7qeBur7Kfi")["items"][i]["track"]["id"])
    print(spotifyObject_1.user_playlist_tracks(playlist_id="4QGhaoFzUW8m7qeBur7Kfi")["items"][99]["track"])
 
    s = 0
    cap = cv2.VideoCapture(0)
    while True:
        _,frame = cap.read()
        boxes, probs = yolo.predict(frame, DEFAULT_THRESHOLD)
        labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
        # 4. save detection result
        frame = draw_scaled_boxes(frame, boxes, probs, config['model']['labels'])
        label_list = config['model']['labels']
        cv2.imshow("imageo", frame)
        cv2.waitKey(1)

        if 1 in labels:
            if spotifyObject_1.currently_playing()["item"]["id"] not in a:
                spotifyObject_1.user_playlist_add_tracks(user=USERNAME ,playlist_id="4QGhaoFzUW8m7qeBur7Kfi",tracks=[spotifyObject_1.currently_playing()["item"]["id"]])
        
       
        #for x in boxes:
            # if config['model']['labels'] == "openhand":
                # print("hehe")
                # if x[0] > 250:
                #     time.sleep(3)
                #     spotifyObject.previous_track()
                # elif x[0] < 50:
                #     time.sleep(3)
                #     spotifyObject.next_track()
    cv2.destroyAllWindows()
            