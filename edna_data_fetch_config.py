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

a = EdnaFetchConfig()
print(a)