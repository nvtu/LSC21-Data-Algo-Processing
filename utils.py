import os
import datetime


def create_folder(folder_abs_path: str):
    if not os.path.exists(folder_abs_path):
        os.makedirs(folder_abs_path)


def get_image_id(image_path: str):
    image_id = os.path.splitext(os.path.basename(image_path))[0]
    return image_id


def preprocess_dict_keys(d):
    ids = list(d.keys())
    for id in ids:
        image_id = get_image_id(id) 
        d[image_id] = d.pop(id)
    return d


def get_week_day(date):
    """
    Get the week day based on date. 
    The date should be in the format YYYY_MM_DD.
    """
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    index = dt.weekday()
    return week_days[index]


def get_month(date):
    """
    Get the month based on date. 
    The date should be in the format YYYY_MM_DD.
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    return months[dt.month - 1]


def get_year(date):
    """
    Get year base on date
    The date should be in the format YYYY_MM_DD
    """
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    return dt.year


def part_of_day(time):
    """
    Determine the part of the day based on the time.
    The user might be careful of the current timezone that you are choosing.
    The time should be considered to be converted to UTC time for convenient of time synchronization between data.
    """
    pod = ['', 'early morning', 'morning', 'late morning', 'early afternoon', 'afternoon', 'late afternoon', 'early evening', 'evening', 'night']
    index = 0
    if datetime.time(4, 0, 0) <= time <= datetime.time(7, 59, 0):
        index = 1
    elif datetime.time(8, 0, 0) <= time <= datetime.time(10, 59, 0):
        index = 2
    elif datetime.time(11, 0, 0) <= time <= datetime.time(11, 59, 0):
        index = 3
    elif datetime.time(12, 0, 0) <= time <= datetime.time(12, 59, 0):
        index = 5
    elif datetime.time(13, 0, 0) <= time <= datetime.time(15, 59, 0):
        index = 4
    elif datetime.time(16, 0, 0) <= time <= datetime.time(16, 59, 0):
        index = 6
    elif datetime.time(17, 0, 0) <= time <= datetime.time(18, 59, 0):
        index = 7
    elif datetime.time(19, 0, 0) <= time <= datetime.time(20, 59, 0):
        index = 8
    elif datetime.time(21, 0, 0) <= time or time <= datetime.time(3, 59, 0):
        index = 9
    return pod[index]


def time_this(func):
    def calc_time(*args, **kwargs):
        before = datetime.datetime.now()
        x = func(*args, **kwargs)
        after = datetime.datetime.now()
        print("Function {} elapsed time: {}".format(func.__name__, after-before))
        return x
    return calc_time