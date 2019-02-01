import json


class EdnaFetchConfigEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == 'EdnaFetchConfig':
            return obj.getDict()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
