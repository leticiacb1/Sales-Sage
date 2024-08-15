import datetime

def get_weekday(date: str) -> int:
    """
        Recive a date in string format and return the weekday 
        correspondent to that day.

        [INPUT]  date : string (Ex: "2022-08-17")

        [OUTPUT] weekday : integer    
            {monday: 0 , thursday: 1 , ... , sunday: 6}
    """

    split_date = date.split('-')
    
    year = int(split_date[0])
    month = int(split_date[1])
    day = int(split_date[2])

    date = datetime.date(year, month, day)
    day_of_week = date.weekday()
    return day_of_week

def get_day(date: str) -> int:
    """
        Recive a date in string format and return the day of that date.

        [INPUT]  date : string (Ex: "2022-08-17")

        [OUTPUT] day : int     (Ex: 17)
    """

    split_date = date.split('-')
    day = split_date[-1]
    return int(day)
    
def get_month(date: str) -> int:
    """
        Recive a date in string format and return the month of that date.

        [INPUT]  date : string (Ex: "2022-08-17")

        [OUTPUT] month : int   (Ex: 8)
    """

    split_date = date.split('-')
    month = split_date[1]
    return int(month)

def get_year(date: str) -> int:
    """
        Recive a date in string format and return the year of that date.

        [INPUT]  date : string (Ex: "2022-08-17")

        [OUTPUT] year : int    (Ex: 2022)
    """

    split_date = date.split('-')
    year = split_date[0]
    return int(year)