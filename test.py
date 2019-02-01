from edna_data_fetch_config import EdnaFetchConfig
from edna_data_fetch_config_encoder import EdnaFetchConfigEncoder
import json

a = EdnaFetchConfig()
print(a)

b = json.dumps(a.getDict())

print(b)

c = EdnaFetchConfig()
c = c.fromDict(json.loads(b))