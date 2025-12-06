import json

def loadjson():
    with open("news.json", "r", encoding="UTF-8") as f:
        return json.load(f)