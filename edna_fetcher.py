from edna_result import EdnaResult
from edna_data_fetch_config import EdnaFetchConfig
from edna_meas import EdnaMeas
import datetime as dt
import math
import csv
import os


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


def saveDictsToFile(fetchConfig, dictList):
    # decide file format
    fileFormat = fetchConfig.file_format

    def any_in(a, b): return bool(set(a).intersection(b))
    if any_in(['csv', 'xlsx'], fileFormat) is not True:
        fileFormat = 'csv'

    # get destination folder
    destFolder = fetchConfig.destination

    # derive the time suffix
    timeSuffixStr = ''
    if fetchConfig.is_time_at_end is True:
        timeFormat = fetchConfig.time_format_str
        nowTime = dt.datetime.now()
        try:
            timeSuffixStr = dt.datetime.strftime(nowTime, timeFormat)
        except ValueError:
            timeSuffixStr = dt.datetime.strftime(nowTime, '_%Y_%m_%d_%H_%M_%S')

    # derive the filename
    fileName = fetchConfig.name + timeSuffixStr
    keys = dictList[0].keys()

    # derive the full filename
    fullFileName = os.path.join(destFolder, fileName + "." + fileFormat)

    # dump the file
    with open(fullFileName, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictList)
