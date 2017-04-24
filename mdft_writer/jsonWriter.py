import json


class JsonWriter:
    "Definition of a JSON file writer"
    def __init__(self, infos = {}):
        self.infos = infos

    def write(self, json_file):
        with open(json_file, 'w') as fjson:
            json.dump(self.infos, fjson, indent = 4)
