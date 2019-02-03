import datetime as dt


class EdnaResult:
    time = dt.datetime(1970, 1, 1, 0, 0, 0)
    val = None
    qual = "init"

    def getDict(self):
        return{
            "val": self.val,
            "qual": self.qual,
            "time": dt.datetime.strftime(self.time, '%Y-%m-%d %H:%M:%S')
        }

    def fromDict(self, dictObj):
        res = EdnaResult()
        keys = [str(keyStr) for keyStr in dictObj.keys()]
        if 'val'in keys:
            res.val = dictObj['val']
        if 'qual'in keys:
            res.qual = dictObj['qual']
        if 'time'in keys:
            res.time = dt.datetime.strptime(
                dictObj['time'], '%Y-%m-%d %H:%M:%S')
