from edna_meas import EdnaMeas
from variable_time import VariableTime


class EdnaFetchConfig:
    name = "name"
    meas_list = []
    from_time = VariableTime()
    to_time = VariableTime()
    sampling_time_secs = 60
    sampling_strategy = "snap"
    is_time_at_end = True
    time_format_str = "_%Y_%m_%d_%H_%M_%S"
    destination = ""
    file_format = "csv"
    host = "wmrm0mc1"
    port = 86448

    def getDict(self):
        return{
            "name": self.name,
            "meas_list": [meas.getDict() for meas in self.meas_list],
            "from_time": self.from_time.getDict(),
            "to_time": self.to_time.getDict(),
            "sampling_time_secs": self.sampling_time_secs,
            "sampling_strategy": self.sampling_strategy,
            "is_time_at_end": self.is_time_at_end,
            "time_format_str": self.time_format_str,
            "destination": self.destination,
            "file_format": self.file_format,
            "host": self.host,
            "port": self.port
        }

    def fromDict(self, dictObj):
        configObj = EdnaFetchConfig()
        keys = [str(keyStr) for keyStr in dictObj.keys()]
        if 'name'in keys:
            configObj.name = dictObj['name']
        if 'meas_list' in keys:
            measObjs = []
            for measDict in dictObj['meas_list']:
                meas = EdnaMeas()
                meas.fromDict(measDict)
                measObjs.append(meas)
            configObj.meas_list = measObjs
        if 'from_time' in keys:
            fromTime = VariableTime()
            fromTime.fromDict(dictObj['from_time'])
            configObj.from_time = fromTime
        if 'to_time' in keys:
            toTime = VariableTime()
            toTime.fromDict(dictObj['to_time'])
            configObj.to_time = toTime
        if 'sampling_time_secs' in keys:
            configObj.sampling_time_secs = dictObj['sampling_time_secs']
        if 'sampling_strategy' in keys:
            configObj.sampling_strategy = dictObj['sampling_strategy']
        if 'is_time_at_end' in keys:
            configObj.is_time_at_end = dictObj['is_time_at_end']
        if 'time_format_str' in keys:
            configObj.time_format_str = dictObj['time_format_str']
        if 'destination' in keys:
            configObj.destination = dictObj['destination']
        if 'file_format' in keys:
            configObj.file_format = dictObj['file_format']
        if 'host' in keys:
            configObj.host = dictObj['host']
        if 'port' in keys:
            configObj.port = dictObj['port']
        return configObj