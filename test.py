from edna_data_fetch_config import EdnaFetchConfig
from edna_data_fetch_config_encoder import EdnaFetchConfigEncoder
from edna_result import EdnaResult
import json
import datetime as dt
from edna_fetcher import fetchDataTest, getDFFromResObj, saveDfToFile
from edna_meas import EdnaMeas

a = EdnaFetchConfig()
a.name = "template_name"
a.is_time_at_end = True
a.time_format_str = "_%Y_%m_%d"
a.destination = 'C:\\Users\\Nagasudhir\\Documents'
a.file_format = 'xlsx'
meas1 = EdnaMeas()
meas1.name = 'name1'
meas2 = EdnaMeas()
meas2.name = 'name2'
a.meas_list = [meas1, meas2]
print(a)

b = json.dumps(a.getDict())

# print(b)

c = EdnaFetchConfig()
c = c.fromDict(json.loads(b))

res = EdnaResult()
resStr = json.dumps(res.getDict())
res2 = json.loads(resStr)
# print(resStr)

a.from_time.abs_time = dt.datetime.now()-dt.timedelta(minutes=10)
a.to_time.abs_time = dt.datetime.now()-dt.timedelta(minutes=5)
a.from_time.mins_offset = -10
a.to_time.mins_offset = -5

resObj = fetchDataTest(a)
resDf = getDFFromResObj(resObj)

saveDfToFile(a, resDf)
