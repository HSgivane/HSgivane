import telebot
from telebot import types
from Config import *
from data import *
from database import *


def sms_start():
    date_info = data()
    chislo = str(date_info[0]) + '.' + str(date_info[1])
    week = date_info[2]
    dayy = int(date_info[3])
    day_n = day_name(dayy)
    week_txt = chet_txt(date_info[2])
    sms_start = f'{bvt} {day_n} \n№{date_info[2]} {week_txt}'
    return sms_start


def knopka():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Monday")
    btn2 = types.KeyboardButton("/Tuesday")
    btn3 = types.KeyboardButton("/Wednesday")
    btn4 = types.KeyboardButton("/Thursday")
    btn5 = types.KeyboardButton("/Friday")
    btn6 = types.KeyboardButton("/Saturday")
    btn7 = types.KeyboardButton("/week")
    btn8 = types.KeyboardButton("/nextweek")
    return markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)    


bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = knopka()
    bot.send_message(message.chat.id, start_msg, reply_markup=markup)
    

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    markup = knopka()
    bot.send_message(message.chat.id, mtuci, reply_markup=markup)


@bot.message_handler(commands=['help'])
def start_message(message):
    markup = knopka()
    bot.send_message(message.chat.id, command_list, reply_markup=markup)


@bot.message_handler(commands=['today'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_num = data_info[3]
    week_num = chet_num(data_info[2])
    day_n = day_name(day_num)
    day_txt = day_go(day_num, week_num, cur)
    text = f'РАСПИСАНИЕ НА СЕГОДНЯ \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    

@bot.message_handler(commands=['tomorrow'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_num = data_info[3]
    week_num = chet_num(data_info[2])
    day_n = day_name(day_num)
    if day_num != 7:
        day_num = day_num+1
    else:
        day_num = 1
    day_txt = day_go(day_num, week_num, cur)
    text = f'РАСПИСАНИЕ НА ЗАВТРА \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    
@bot.message_handler(commands=['week'])
def start_message(message):
    markup = knopka()
    day_txt = ''
    data_info = data()  
    week_num = chet_num(data_info[2])
    for i in range(1,7):
        day_n = day_name(i)
        day_txt1 = day_go(i, week_num, cur)
        day_txt1 = day_n + '\n' + day_txt1
        day_txt = day_txt + '\n' + day_txt1 + '\n ____________________ \n'
    text = f'РАСПИСАНИЕ НА НЕДЕЛЮ \n{sms_start()} \n\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['nextweek'])
def start_message(message):
    markup = knopka()
    data_info = data()
    week = data_info[2]
    week_num = chet_num(data_info[2])
    if week_num == 1: 
        week_num = 2
    else: 
        week_num = 1
    week_txt = chet_txt(week_num)
    day_txt = f'Отображено расписание на следующую неделю \n№{week+1} {week_txt.upper()}'
    for i in range(1,7):
        day_n = day_name(i)
        day_txt1 = day_go(i, week_num, cur)
        day_txt1 = day_n + '\n' + day_txt1
        day_txt = day_txt + '\n' + day_txt1 + '\n ____________________ \n'
    text = f'РАСПИСАНИЕ НА СЛЕДУЮЩУЮ НЕДЕЛЮ \n{sms_start()} \n\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['Monday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Понедельник'
    week_num = chet_num(data_info[2])
    day_txt = day_go(1, week_num, cur)
    text = f'РАСПИСАНИЕ НА ПОНЕДЕЛЬНИК \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['Tuesday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Вторник'
    week_num = chet_num(data_info[2])
    day_txt = day_go(2, week_num, cur)
    text = f'РАСПИСАНИЕ НА ВТОРНИК \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['Wednesday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Среда'
    week_num = chet_num(data_info[2])
    day_txt = day_go(3, week_num, cur)
    text = f'РАСПИСАНИЕ НА СРЕДУ \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    

@bot.message_handler(commands=['Thursday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Четверг'
    week_num = chet_num(data_info[2])
    day_txt = day_go(4, week_num, cur)
    text = f'РАСПИСАНИЕ НА ЧЕТВЕРГ \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    

@bot.message_handler(commands=['Friday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Пятница'
    week_num = chet_num(data_info[2])
    day_txt = day_go(5, week_num, cur)
    text = f'РАСПИСАНИЕ НА ПЯТНИЦУ \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['Saturday'])
def start_message(message):
    markup = knopka()
    data_info = data()
    day_n = 'Суббота'
    week_num = chet_num(data_info[2])
    day_txt = day_go(6, week_num, cur)
    text = f'РАСПИСАНИЕ НА Субботу \n{sms_start()} \n\n{day_n}\n{day_txt}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    markup = knopka()
    bot.send_message(message.chat.id, 'Извините, я Вас не понял', reply_markup=markup)


bot.infinity_polling(none_stop=True,interval=0)
