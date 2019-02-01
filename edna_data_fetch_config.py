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
    time_format_str = ""
    destination = ""
    file_format = "csv"

    def getDict(self):
        return{
            'name': self.name,
            'meas_list': [meas.getDict() for meas in self.meas_list],
            'from_time': self.from_time.getDict(),
            'to_time': self.to_time.getDict(),
            'sampling_time_secs': self.sampling_time_secs,
            'sampling_strategy': self.sampling_strategy,
            'is_time_at_end': self.is_time_at_end,
            'time_format_str': self.time_format_str,
            'destination': self.destination,
            'file_format': self.file_format
        }
