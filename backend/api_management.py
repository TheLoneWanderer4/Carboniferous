import json
default_key_loc = "api_keys.json"

class APIKeys:
    google_key = ""
    lutf_main_key = ""
    lutf_private_key = ""
    def __init__(self, key_loc = default_key_loc):
        keys = json.load(open(key_loc))
        self.google_key = keys["GoogleMaps"]
        self.lutf_main_key = keys["LuftMain"]
        self.lutf_private_key = keys["LuftPrivate"]

    @staticmethod
    def get_google_key(self):
        return self.google_key

    @staticmethod
    def get_lutf_main_key(self):
        return self.lutf_main_key

    @staticmethod
    def get_lutf_private_key(self):
        return self.lutf_private_key