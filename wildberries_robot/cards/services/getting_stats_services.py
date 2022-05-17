from datetime import datetime
import pytz


def getting_params(params):
    start_date = params.get('start')
    end_date = params.get('end')
    interval = int(params.get('interval', 1))
    return param_time_to_datetime(start_date), param_time_to_datetime(end_date), interval


def param_time_to_datetime(str_of_time):
    str_of_time = datetime.strptime(str_of_time, '%Y-%m-%d')
    timezone_time = pytz.utc.localize(str_of_time, is_dst=None).astimezone()
    return timezone_time.replace(minute=0, second=0, microsecond=0)
