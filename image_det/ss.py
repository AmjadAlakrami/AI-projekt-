import json, socket    

DEFAULT_CONFIG_FILE = "./image_det/config.json"
config_buffer = open(DEFAULT_CONFIG_FILE,'r') 
config = json.loads(config_buffer.read())
hostname = socket.gethostname()    

e =[]
for i in range(0, len(config["spotify_config"]["Devices"])): 
    e.append(config["spotify_config"]["Devices"][i]["devuce-name"])

print(e)
if hostname in e:
    print(config["spotify_config"]["Devices"][e.index(hostname)]["devuce-name"])
