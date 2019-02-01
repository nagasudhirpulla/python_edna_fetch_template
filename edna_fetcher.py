from edna_result import EdnaResult
from edna_data_fetch_config import EdnaFetchConfig
from edna_meas import EdnaMeas
import datetime as dt
import math


def fetchDataTest(fetchConfig):
    from_time = fetchConfig.from_time.getTime()
    to_time = fetchConfig.to_time.getTime()
    resList = []
    for iter in range(int((to_time-from_time).total_seconds()/60)):
        res = EdnaResult()
        res.val = iter
        res.time = from_time + dt.timedelta(minutes=iter)
        resList.append(res)
    return resList
