import json
default_key_loc = "api_keys.json"

class APIKeys:
    google_key_val = ""
    lutf_main_key_val = ""
    lutf_private_key_val = ""
    def __init__(self, key_loc = default_key_loc):
        keys = json.load(open(key_loc))
        self.google_key_val = keys["GoogleMaps"]
        self.lutf_main_key_val = keys["LuftMain"]
        self.lutf_private_key_val = keys["LuftPrivate"]

    def google_key(self):
        return self.google_key_val

    def luft_main_key(self):
        return self.lutf_main_key_val

    def luft_private_key(self):
        return self.lutf_private_key_val