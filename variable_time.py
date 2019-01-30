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
            'abs_time': self.abs_time,
            'abs_time_format': self.abs_time_format,
            'years_offset': self.years_offset,
            'months_offset': self.months_offset,
            'days_offset': self.days_offset,
            'hours_offset': self.hours_offset,
            'mins_offset': self.mins_offset,
            'secs_offset': self.secs_offset,
            'is_years_variable': self.is_years_variable,
            'is_months_variable': self.is_months_variable,
            'is_days_variable': self.is_days_variable,
            'is_hours_variable': self.is_hours_variable,
            'is_mins_variable': self.is_mins_variable,
            'is_secs_variable': self.is_secs_variable
        }