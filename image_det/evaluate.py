import json, cv2, os, spotipy, yolo, time, json, os.path, socket  
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
import spotipy.util as util

DEFAULT_CONFIG_FILE = "./image_det/config.json"
DEFAULT_WEIGHT_FILE = "./image_det/model.h5"
config_buffer = open(DEFAULT_CONFIG_FILE,'r') 
config = json.loads(config_buffer.read())

a = []
s = []
e = []

w = 0
spotifyObject_1= None
# 2. create yolo instance & predict
yolo = create_yolo(config['model']['architecture'],
                    config['model']['labels'],
                    config['model']['input_size'],
                    config['model']['anchors'])
yolo.load_weights(DEFAULT_WEIGHT_FILE)
hostname = socket.gethostname() 
def Connect_to_token(): #ansluter till spotify token 
    global spotifyObject_1, e
    for i in range(0, len(config["spotify_config"]["Devices"])): 
        e.append(config["spotify_config"]["Devices"][i]["devuce-name"])
    if hostname in e:
         config["spotify_config"]["USERNAME"] = config["spotify_config"]["Devices"][e.index(hostname)]["USERNAME"]
    else:
        config["spotify_config"]["USERNAME"] = input("Enter your spotify username: ")
        config["spotify_config"]["Devices"].append(      
             {
            "devuce-name": hostname,
            "USERNAME": config["spotify_config"]["USERNAME"]
            })
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)
    if os.path.isfile(".cache-"+ config["spotify_config"]["USERNAME"]):#förnya genom att tabort den gamla token 
        os.remove(".cache-"+ config["spotify_config"]["USERNAME"])
    token_1= util.prompt_for_user_token(username=config["spotify_config"]["USERNAME"], scope=config["spotify_config"]["SCOPE"],client_id=config["spotify_config"]["SPOTIPY_CLIENT_ID"], redirect_uri=config["spotify_config"]["SPOTIPY_REDIRECT_URI"], client_secret=config["spotify_config"]["SPOTIPY_CLIENT_SECRET"])
    spotifyObject_1 = spotipy.Spotify(auth=token_1)

def creat_list(): # skapar listan där låtar kommer att läggas till 
    for List in range(0,spotifyObject_1.user_playlists(user=config["spotify_config"]["USERNAME"])["total"]): #hämtar alla listor som användaren har 
        a.append(spotifyObject_1.user_playlists(user=config["spotify_config"]["USERNAME"])["items"][List]["name"])
    if "my super cool AI playlist" not in a: #om my super cool AI playlist inte är skapad förut
        spotifyObject_1.user_playlist_create(user=config["spotify_config"]["USERNAME"], name="my super cool AI playlist", public=False, description="my super cool AI playlist made with my super cool AI program")#skapar spellistan 
        config["spotify_config"]["list_created"] = spotifyObject_1.user_playlists(user=config["spotify_config"]["USERNAME"])["items"][0]["id"]
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)
        print("created")

def Add_to_list():#lägger till låtar till spellistan 
    if spotifyObject_1.currently_playing()["item"]["id"] not in config["spotify_config"]["track_in_list"]: #om låten inte finns i listan 
        config["spotify_config"]["track_in_list"].append(spotifyObject_1.currently_playing()["item"]["id"])
        new_json_string = json.dumps(config, indent=4, )
        config_buffer = open(DEFAULT_CONFIG_FILE,'w+') 
        config_buffer.write(new_json_string)
        spotifyObject_1.user_playlist_add_tracks(user=config["spotify_config"]["USERNAME"] ,playlist_id=config["spotify_config"]["list_created"],tracks=[spotifyObject_1.currently_playing()["item"]["id"]])#lägger till låten i spellistan 
        print("added")      
    else:
        print("track is already in list")

def Change_song_puse_play(): #byter låtar, pausa och spela 
    global s 
    s.append(boxes[0][0]) #lägger till hand positionen i en lista för att kunna jämföra förändringen 
    if s[0]-s[-1] < -200: #om förändringen mellan den första och sista värdet är mindre än -200 så betyder det att handen har rört sig högeråt 
        s = []
        spotifyObject_1.next_track() #spela nästa låt 
        
        time.sleep(0.5)

    elif s[0]-s[-1] > 200: #om förändringen mellan den första och sista värdet är mindre än -200 så betyder det att handen har rört sig vänsteråt  
        s = []
        spotifyObject_1.previous_track() #spelar föregånde låt 
        time.sleep(0.5)
    
    elif len(s) > 40: #om listans längd är större än 40
        if s[0]-s[1] < 25 and s[0]-s[1] > -25 : #och skillnaden mellan den första och sista värdet är mellan 25 och -25 (det betyder att handen inte rör på sig)
            if not spotifyObject_1.currently_playing()["is_playing"]: # spela om musiken är pausad
                spotifyObject_1.start_playback()
                time.sleep(0.5)
            elif spotifyObject_1.currently_playing()["is_playing"]:# spela om musiken är pausad 
                spotifyObject_1.pause_playback()
                time.sleep(0.5)
        s = []

cap = cv2.VideoCapture(0)
Connect_to_token()
creat_list()
while True:
    _,frame = cap.read() 
    #startar detektering
    boxes, probs = yolo.predict(frame, config["model"]["DEFAULT_THRESHOLD"]) 
    labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
    #sparar detekterings resultat 
    frame = draw_scaled_boxes(frame, boxes, probs, config['model']['labels'])
    label_list = config['model']['labels']
    cv2.imshow("imageo", frame)
    cv2.waitKey(1)


    if 0 in labels: #om en tummeup hittas 
        try:
            Add_to_list()
        except:
            input(" No active device found ... press ENTER when you are back on track")
    if 1 in labels: #om en hand hittas
        
            Change_song_puse_play()



cv2.destroyAllWindows()
        