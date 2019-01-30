from edna_data_fetch_config import EdnaFetchConfig
from edna_data_fetch_config_encoder import EdnaFetchConfigEncoder
import json

a = EdnaFetchConfig()
print(a)

b = json.dumps(a, cls=EdnaFetchConfigEncoder)

print(b)