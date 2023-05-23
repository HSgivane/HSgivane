from datetime import date
import calendar

def data():
    data = date.today()
    dt = str(data)
    day = int(dt[8:10])
    month = int(dt[5:7])
    week = data.isocalendar()[1]
    day_name = calendar.day_name[data.weekday()]
    if day_name == 'Monday': day_name = 1
    elif day_name == 'Tuesday': day_name = 2
    elif day_name == 'Wednesday': day_name = 3
    elif day_name == 'Thursday': day_name = 4
    elif day_name == 'Friday': day_name = 5
    elif day_name == 'Saturday': day_name = 6
    elif day_name == 'Sunday': day_name = 7
    return (day, month, week-4, day_name)

def day_name(day):
    if day == 1: day_name = 'Понедельник'
    elif day == 2: day_name = 'Вторник'
    elif day == 3: day_name = 'Среда'
    elif day == 4: day_name = 'Четверг'
    elif day == 5: day_name = 'Пятница'
    elif day == 6: day_name = 'Суббота'
    elif day == 7: day_name = 'Воскресенье'  
    return day_name

def chet_txt(week):
    if week%2 == 1: n_txt_week = 'нечетная'
    else: n_txt_week = 'четная'
    return n_txt_week

def chet_num(week):
    if week%2 == 1: n_num_week = 1
    else: n_num_week = 2
    return n_num_week
