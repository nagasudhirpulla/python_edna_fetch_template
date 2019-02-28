
from edna_result import EdnaResult
from edna_data_fetch_config import EdnaFetchConfig
from edna_meas import EdnaMeas
import datetime as dt
import math
import csv
import os
import xlsxwriter
import numpy as np
import pandas as pd
import requests
import json

from pandas import ExcelWriter


def fetchPntData(pnt, req_time):
    req_date_str = req_time.strftime('%d/%m/%Y')
    # print(req_date_str)
    params = dict(
        pnt=pnt,
        strtime="{0}/00:00:00".format(req_date_str),
        endtime="{0}/{1}:{2}:00".format(req_date_str, makeTwoDigits(
            req_time.hour), makeTwoDigits(req_time.minute)),
        secs="300",
        type="average"
    )
    r = requests.get(
        url="http://wmrm0mc1:62448/api/values/history", params=params)
    data = json.loads(r.text)
    return data


def fetchDataTest(fetchConfig):
    from_time = fetchConfig.from_time.getTime()
    to_time = fetchConfig.to_time.getTime()
    resObj = {}
    # initializing the result object
    for meas in fetchConfig.meas_list:
        resObj[meas.name] = []

    for meas in fetchConfig.meas_list:
        resList = []
        for iter in range(int((to_time-from_time).total_seconds()/60)):
            res = EdnaResult()
            res.val = iter
            res.time = from_time + dt.timedelta(minutes=iter)
            resList.append(res)
        resObj[meas.name] = resList
    return resObj


def getDumpFileName(fetchConfig):
    # decide file format
    fileFormat = fetchConfig.file_format

    def any_in(a, b): return bool(set(a).intersection(b))
    if any_in(['csv', 'xlsx'], [fileFormat]) is not True:
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

    # derive the full filename
    fullFileName = os.path.join(destFolder, fileName + "." + fileFormat)
    return fullFileName


def getDFFromResObj(resObj):
    # get all the keys of the resObj and initialize a dataframe
    measNames = list(resObj.keys())
    # initialize the result DataFrame
    resDf = pd.DataFrame(columns=measNames)
    for measName in measNames:
        measDataObjs = resObj[measName]
        # convert this list of edna results to pandas series
        seriesObj = {}
        for dataObj in measDataObjs:
            seriesObj[dataObj.time] = dataObj.val
        measSeries = pd.Series(seriesObj)
        resDf[measName] = measSeries
    resDf.index.name = 'time'
    return resDf


def saveDfToFile(fetchConfig, df):
    fileName = getDumpFileName(fetchConfig)

    # dump the file
    if fileName.endswith('xlsx'):
        writer = ExcelWriter(fileName)
        df.to_excel(writer)
        writer.save()
    else:
        df.to_csv(fileName, sep=',')


def makeTwoDigits(num):
    if(num < 10):
        return "0"+str(num)
    return num
