from datetime import datetime


def validate_date(date_string):
    """
    chech if the date is 'yyyymmdd' format
    :param date_string:
    :return:
    """
    try:
        datetime.strptime(date_string, '%Y%m%d')
        return True
    except ValueError:
        return False
