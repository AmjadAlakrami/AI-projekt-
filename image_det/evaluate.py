import json, cv2, os, spotipy, yolo, time
import cv2
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
import spotipy.util as util

DEFAULT_CONFIG_FILE = os.path.join("C:/Users/s8amjala/Desktop/AI-projekt-/image_det", "config.json")
DEFAULT_WEIGHT_FILE = os.path.join("C:/Users/s8amjala/Desktop/AI-projekt-/image_det", "Model.h5")
DEFAULT_THRESHOLD = 0.4

SPOTIPY_CLIENT_ID='830e5bf515504d4293f128fe0fa77191'
SPOTIPY_CLIENT_SECRET='abd8c43c229342dbbfff672a04f6d132'
SPOTIPY_REDIRECT_URI='https://www.google.com/'
USERNAME ="wj4xvcjslfruo3tv9wl1nq0rw"
SCOPE = "user-modify-playback-state"

if __name__ == '__main__':
    try:
        token = util.prompt_for_user_token(username=USERNAME, scope=SCOPE, client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)
    except:
        os.remove(".cache-"+USERNAME)
        token = util.prompt_for_user_token(username=USERNAME, scope=SCOPE, client_id=SPOTIPY_CLIENT_ID, redirect_uri=SPOTIPY_REDIRECT_URI, client_secret=SPOTIPY_CLIENT_SECRET)
    spotifyObject = spotipy.Spotify(auth=token)

    with open(DEFAULT_CONFIG_FILE) as config_buffer:
        config = json.loads(config_buffer.read())

    # 2. create yolo instance & predict
    yolo = create_yolo(config['model']['architecture'],
                       config['model']['labels'],
                       config['model']['input_size'],
                       config['model']['anchors'])
    yolo.load_weights(DEFAULT_WEIGHT_FILE )

    

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
        print(config['model']['labels'])
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
            