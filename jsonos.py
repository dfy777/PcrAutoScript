import json
import os

LOCATION_JSON_PATH = "location.json"

def ReadJson(name=False):
    with open(LOCATION_JSON_PATH, "r") as load_f:
        load_dict = json.load(load_f)
        if (name):
            return load_dict[name]
        else:
            return load_dict


def WriteJson(name, location):
    ptx, pty, inc_x, inc_y = location[:4]
    js_dict = {}
    with open(LOCATION_JSON_PATH, 'r') as load_f:
        js_dict = json.load(load_f)
    
    js_dict[name] = (ptx, pty, inc_x, inc_y)
    
    with open(LOCATION_JSON_PATH, 'w') as write_f:
        json.dump(js_dict, write_f, indent=4, separators=[',', ':'])


def InitializeJson():
    js_dict = {}
    with open(LOCATION_JSON_PATH, 'r') as load_f:
        js_dict = json.load(load_f)

    for key in js_dict:
        js_dict[key] = (-1, -1, -1, -1)
    
    with open(LOCATION_JSON_PATH, 'w') as write_f:
        json.dump(js_dict, write_f, indent=4, separators=[',', ':'])