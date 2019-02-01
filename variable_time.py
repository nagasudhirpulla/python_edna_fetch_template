class VariableTime:
    abs_time = ""
    abs_time_format = ""
    years_offset = 0
    months_offset = 0
    days_offset = 0
    hours_offset = 0
    mins_offset = 0
    secs_offset = 0
    is_years_variable = True
    is_months_variable = True
    is_days_variable = True
    is_hours_variable = True
    is_mins_variable = True
    is_secs_variable = True

    def getDict(self):
        return {
            "abs_time": self.abs_time,
            "abs_time_format": self.abs_time_format,
            "years_offset": self.years_offset,
            "months_offset": self.months_offset,
            "days_offset": self.days_offset,
            "hours_offset": self.hours_offset,
            "mins_offset": self.mins_offset,
            "secs_offset": self.secs_offset,
            "is_years_variable": self.is_years_variable,
            "is_months_variable": self.is_months_variable,
            "is_days_variable": self.is_days_variable,
            "is_hours_variable": self.is_hours_variable,
            "is_mins_variable": self.is_mins_variable,
            "is_secs_variable": self.is_secs_variable
        }

    def fromDict(self, dictObj):
        configObj = VariableTime()
        keys = [str(keyStr) for keyStr in dictObj.keys()]
        if 'abs_time'in keys:
            configObj.abs_time = dictObj['abs_time']
        if 'abs_time_format'in keys:
            configObj.abs_time_format = dictObj['abs_time_format']
        if 'years_offset'in keys:
            configObj.years_offset = dictObj['years_offset']
        if 'months_offset'in keys:
            configObj.months_offset = dictObj['months_offset']
        if 'days_offset'in keys:
            configObj.days_offset = dictObj['days_offset']
        if 'hours_offset'in keys:
            configObj.hours_offset = dictObj['hours_offset']
        if 'mins_offset'in keys:
            configObj.mins_offset = dictObj['mins_offset']
        if 'secs_offset'in keys:
            configObj.secs_offset = dictObj['secs_offset']
        if 'is_years_variable'in keys:
            configObj.is_years_variable = dictObj['is_years_variable']
        if 'is_months_variable'in keys:
            configObj.is_months_variable = dictObj['is_months_variable']
        if 'is_days_variable'in keys:
            configObj.is_days_variable = dictObj['is_days_variable']
        if 'is_hours_variable'in keys:
            configObj.is_hours_variable = dictObj['is_hours_variable']
        if 'is_mins_variable'in keys:
            configObj.is_mins_variable = dictObj['is_mins_variable']
        if 'is_secs_variable'in keys:
            configObj.is_secs_variable = dictObj['is_secs_variable']
        return configObj
