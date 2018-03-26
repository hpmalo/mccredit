# -*- coding: utf-8 -*-
import coms
import telebot
import os
from telebot import types

bot = telebot.TeleBot(coms.token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                    'О нас✅']])
    bot.send_message(m.chat.id, 'Привет я бот Money credit! У меня ты можешь узнать о нашем продукте.',
                     reply_markup=keyboard)
    f = open('DB.txt', 'a')
    f.write(str(m.chat.id) + '\n')

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, '''Бот *Money Credit*
Тут ты можешь заказать займ
Узнать о нас
Напиши команду /start''', parse_mode='Markdown')
@bot.message_handler(regexp='в меню▶')
def menu(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                    'О нас✅']])
    bot.send_message(m.chat.id, 'Moneycredit',
                     reply_markup=keyboard)


@bot.message_handler(regexp='Заем под залог авто🚘')
def car(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Закaзать займ']])
    bot.send_message(m.chat.id,'''*Moneycredit* представляет займы под залог Авто.
    У нас вы сможете получить займ под залог авто без справок и поручителей и с любой кредитной историей.
    От *50.000* до *1.000.000* рублей, сроком от 1 месяца до 36 месяцев с процентной ставкой от 5% в месяц.
    от *50 000* до *500 000* 6% в месяц
    от *500 000* до *1 000 000* 5% в месяц
    Вам необходимо при себе иметь только паспорт, документы на автомобиль.''',parse_mode='Markdown', reply_markup=keyboard)

def car1(m):
    try:
        if 49999 < int(m.text) < 1000001:
            reth=bot.send_message(m.chat.id, '''Теперь введи срок займа в днях *От 1 до 36 месяцев*''', parse_mode='Markdown')
            bot.register_next_step_handler(reth, car2)
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text+'\n')
        else:
            if int(m.text) > 1000000:
                rthree = bot.send_message(m.chat.id, 'Если тебе нужно больше *1 млн* я могу тебе предложить под залог*',
                                          parse_mode='Markdown')
                bot.register_next_step_handler(rthree, car1)
            elif 100000 > int(m.text):
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(*[types.InlineKeyboardButton(text=name,
                                                          callback_data=name) for name in
                               ['Заем под залог авто🚗', 'Потребительские займы💸']])
                rtwor = bot.send_message(m.chat.id, '''Ты ввел сумму меньше чем я могу тебя дать, попробуй ввести снова либо выбери заем под залог авто или потребительский займ''', reply_markup=keyboard)
                bot.register_next_step_handler(rtwor, car1)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
        else:
            thor=bot.send_message(m.chat.id, 'Я не понимаю тебя. Введи сумму от 100.000 до 5.000.000 рублей')
            bot.register_next_step_handler(thor, car1)

def car2(m):
    try:
        if 1 <= int(m.text) <= 36:
            dvar=bot.send_message(m.chat.id, '''Введи *ФИО*''', parse_mode='Markdown')
            bot.register_next_step_handler(dvar, fio)
            g=open('{}.txt'.format(m.chat.id), 'a')
            g.write(m.text+'\n')
        else:
            if int(m.text) > 36:
                fivr=bot.send_message(m.chat.id, 'Ой когда срок больше, нужно общаться с менеджером. Сделай срок меньше')
                bot.register_next_step_handler(fivr, car2)
            elif 1 > int(m.text):
                sixr=bot.send_message(m.chat.id, 'Что то не так введи срок от 1 до 36 месяцев')
                bot.register_next_step_handler(sixr.car2)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            sevr = bot.send_message(m.chat.id, 'Что то не так введи срок от 1 до 36 месяцев')
            bot.register_next_step_handler(sevr, car2)

@bot.message_handler(regexp='Потребительские займы💸')
def zaim(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Заказать займ']])
    bot.send_message(m.chat.id,'''*Условия микрозайма*
    Микрозайм, пожалуй, лучшее решение, когда Вам нужны деньги на срочную покупку, 
а до зарплаты еще далеко. Получить заем может любой житель России в возрасте от 18 до 65 лет,
с регулярным ежемесячным доходом, с адресом проживания и регистрацией в городах присутствия Moneycredit. 
Кредитная история и платежеспособность также будут оцениваться. 
Для получения займа нужен только паспорт и мобильный телефон. 
Заявку можно оформить онлайн, не выходя из дома!''', parse_mode='Markdown', reply_markup=keyboard)

def zaim1(m):
    try:
        if 4999 < int(m.text) < 30001:
            ethr=bot.send_message(m.chat.id, '''Теперь введи срок займа в днях
*От 7 до 30 дней*''', parse_mode='Markdown')
            bot.register_next_step_handler(ethr, zaim2)
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text+'\n')

        else:
            if int(m.text) > 30000:
                threer = bot.send_message(m.chat.id, 'Если тебе нужно больше *30 тысяч* ты можешь оформить под залог *Авто* или *Недвижемости*',
                                          parse_mode='Markdown')
                bot.register_next_step_handler(threer, zaim1)
            elif 5000 > int(m.text):
                 twor = bot.send_message(m.chat.id, '''Ты ввел сумму меньше чем я могу тебя дать, попробуй ввести снова''')
                 bot.register_next_step_handler(twor, zaim1)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
        else:
            thor=bot.send_message(m.chat.id, 'Я не понимаю тебя. Введи сумму от 5000 до 30000 рублей')
            bot.register_next_step_handler(thor, zaim1)


def zaim2(m):
    try:
        if 6 < int(m.text) < 31:
            dvar=bot.send_message(m.chat.id, '''Введи *ФИО*''', parse_mode='Markdown')
            bot.register_next_step_handler(dvar, fio)
            g=open('{}.txt'.format(m.chat.id), 'a')
            g.write(m.text+'\n')
        else:
            if int(m.text) > 30:
                fivr=bot.send_message(m.chat.id, 'Ой когда срок больше месяца, нужно общаться с менеджером. Сделай срок меньше')
                bot.register_next_step_handler(fivr, zaim2)
            elif 7 > int(m.text):
                sixr=bot.send_message(m.chat.id, 'Что то не так введи срок от 7 до 30 дней')
                bot.register_next_step_handler(sixr.zaim2)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            sevr = bot.send_message(m.chat.id, 'Что то не так введи срок от 7 до 30 дней')
            bot.register_next_step_handler(sevr, zaim2)

def fio(m):
    try:
        miss = m.text.replace(' ','')
        if miss.isalpha():
            mma=bot.send_message(m.chat.id, 'Теперь введи номер телефона')
            bot.register_next_step_handler(mma, number)
            a = open('{}.txt'.format(m.chat.id), 'a')
            a.write(m.text+'\n')
        else:
            if m.text == 'в меню▶':
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*[types.KeyboardButton(name) for name in
                               ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                                'О нас✅']])
                bot.send_message(m.chat.id, 'Moneycredit',
                                 reply_markup=keyboard)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
                os.remove(path)
            else:
                trir=bot.send_message(m.chat.id, 'Я тебя не понимаю')
                bot.register_next_step_handler(trir, fio)
    except AttributeError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            trir = bot.send_message(m.chat.id, 'Я тебя не понимаю')
            bot.register_next_step_handler(trir, fio)

def number(m):
    try:
        if m.text.isalnum():
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(*[types.InlineKeyboardButton(text=name,
                                                      callback_data=name) for name in ['✅Заказать этот займ✅']])
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.readlines()
            summ=int(line[0])
            sroc=int(line[1])
            sum=summ//100*0.8*sroc
            bot.send_message(m.chat.id, '''Давай проверим
Тебе нужно *{}* рублей ✅
На срок *{}* дней ✅
Переплата *{}* рублей ✅'''.format(summ, sroc, sum), parse_mode='Markdown', reply_markup=keyboard)
            g = open('{}.txt'.format(m.chat.id), 'a')
            g.write(m.text + '\n')
        else:
            if m.text == 'в меню▶':
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*[types.KeyboardButton(name) for name in
                               ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                                'О нас✅']])
                bot.send_message(m.chat.id, 'Moneycredit',
                                 reply_markup=keyboard)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
                os.remove(path)
            else:
                trir=bot.send_message(m.chat.id, 'Я тебя не понимаю')
                bot.register_next_step_handler(trir, number)
    except AttributeError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            trir = bot.send_message(m.chat.id, 'Я тебя не понимаю')
            bot.register_next_step_handler(trir, number)





@bot.message_handler(regexp='Заем под залог недвижимости🏠')
def dom(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Зaказать займ']])
    bot.send_message(m.chat.id,'''*Moneycredit* представляет займы под залог недвижимости🏠.
    У нас вы сможете получить займ под залог авто без справок и поручителей и с любой кредитной историей.
От *100.000* до *5.000.000* рублей, сроком от 1 месяца до 36 месяцев с процентной ставкой от 4% в месяц.
от *100 000* до *1.000 000* 5% в месяц
от *1.000 000* до *5.000 000* 4% в месяц
Вам необходимо при себе иметь только паспорт, свидетельство и выписку из Росреестра..''',parse_mode='Markdown', reply_markup=keyboard)

def dom1(m):
    try:
        if 99999 < int(m.text) < 5000001:
            reth=bot.send_message(m.chat.id, '''Теперь введи срок займа в днях *От 1 до 36 месяцев*''', parse_mode='Markdown')
            bot.register_next_step_handler(reth, dom2)
            f = open('{}.txt'.format(m.chat.id), 'w+')
            f.write(m.text+'\n')
        else:
            if int(m.text) > 5000000:
                rthree = bot.send_message(m.chat.id, 'Если тебе нужно больше *5 млн* укажи сумму меньше 5, в дальнейшем менеджер расскажет тебе о условиях*',
                                          parse_mode='Markdown')
                bot.register_next_step_handler(rthree, dom1)
            elif 100000 > int(m.text):
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(*[types.InlineKeyboardButton(text=name,
                                                          callback_data=name) for name in
                               ['Заем под залог авто🚗', 'Потребительские займы💸']])
                rtwor = bot.send_message(m.chat.id, '''Ты ввел сумму меньше чем я могу тебя дать, попробуй ввести снова либо выбери заем под залог авто или потребительский займ''', reply_markup=keyboard)
                bot.register_next_step_handler(rtwor, dom1)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
        else:
            thor=bot.send_message(m.chat.id, 'Я не понимаю тебя. Введи сумму от 100.000 до 5.000.000 рублей')
            bot.register_next_step_handler(thor, dom1)

def dom2(m):
    try:
        if 1 <= int(m.text) < 37:
            dvar=bot.send_message(m.chat.id, '''Введи *ФИО*''', parse_mode='Markdown')
            bot.register_next_step_handler(dvar, fio1)
            g=open('{}.txt'.format(m.chat.id), 'a')
            g.write(m.text+'\n')
        else:
            if int(m.text) > 36:
                fivr=bot.send_message(m.chat.id, 'Ой когда срок больше, нужно общаться с менеджером. Сделай срок меньше, дальще менеджер тебе объяснит')
                bot.register_next_step_handler(fivr, dom2)
            elif 1 >= int(m.text):
                sixr=bot.send_message(m.chat.id, 'Что то не так введи срок от 1 до 36 месяцев')
                bot.register_next_step_handler(sixr.dom2)
    except ValueError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            sevr = bot.send_message(m.chat.id, 'Что то не так введи срок от 1 до 36 месяцев')
            bot.register_next_step_handler(sevr, dom2)

def fio1(m):
    try:
        miss = m.text.replace(' ','')
        if miss.isalpha():
            mma=bot.send_message(m.chat.id, 'Теперь введи номер телефона')
            bot.register_next_step_handler(mma, number1)
            a = open('{}.txt'.format(m.chat.id), 'a')
            a.write(m.text+'\n')
        else:
            if m.text == 'в меню▶':
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*[types.KeyboardButton(name) for name in
                               ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                                'О нас✅']])
                bot.send_message(m.chat.id, 'Moneycredit',
                                 reply_markup=keyboard)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
                os.remove(path)
            else:
                trir=bot.send_message(m.chat.id, 'Я тебя не понимаю')
                bot.register_next_step_handler(trir, fio)
    except AttributeError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            trir = bot.send_message(m.chat.id, 'Я тебя не понимаю')
            bot.register_next_step_handler(trir, fio)

def number1(m):
    try:
        if m.text.isalnum():
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(*[types.InlineKeyboardButton(text=name,
                                                      callback_data=name) for name in ['✅Заказать этот займ✅']])
            f = open('{}.txt'.format(m.chat.id), 'r')
            line = f.readlines()
            summ=int(line[0])
            sroc=int(line[1])
            if summ >= 1000000:
                sum=summ//100*4*sroc
                ejm=summ//100*4
            else:
                sum = summ // 100 * 5 * sroc
                ejm = summ // 100 * 5
            bot.send_message(m.chat.id, '''Давай проверим
Тебе нужно *{}* рублей ✅
На срок *{}* месяцев ✅
Переплата *{}* рублей ✅
Плата в месяц *{}*'''.format(summ, sroc, sum, ejm), parse_mode='Markdown', reply_markup=keyboard)
            g = open('{}.txt'.format(m.chat.id), 'a')
            g.write(m.text + '\n')
        else:
            if m.text == 'в меню▶':
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*[types.KeyboardButton(name) for name in
                               ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                                'О нас✅']])
                bot.send_message(m.chat.id, 'Moneycredit',
                                 reply_markup=keyboard)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
                os.remove(path)
            else:
                trir=bot.send_message(m.chat.id, 'Я тебя не понимаю')
                bot.register_next_step_handler(trir, number)
    except AttributeError:
        if m.text == 'в меню▶':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(name) for name in
                           ['Потребительские займы💸', 'Заем под залог недвижимости🏠', 'Заем под залог авто🚘',
                            'О нас✅']])
            bot.send_message(m.chat.id, 'Moneycredit',
                             reply_markup=keyboard)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(m.chat.id))
            os.remove(path)
        else:
            trir = bot.send_message(m.chat.id, 'Я тебя не понимаю')
            bot.register_next_step_handler(trir, number)

@bot.message_handler(regexp='О нас✅')
def faq(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Где мы находимся']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Документация']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,
                                              callback_data=name) for name in ['Инвестировать']])
    bot.send_message(m.chat.id, ''' *MoneyCredit*
Это доступный способ получить наличные деньги в заем быстро и с минимальным пакетом документов. Мы стремимся обеспечить наилучший сервис, поэтому для постоянных клиентов доступны большие суммы займов и с меньшей процентной ставкой.
Каждую заявку мы рассматриваем индивидуально, поэтому Вы можете получить деньги даже с чистой или испорченной кредитной историей!

Звоните нам:
*+78432533375*
Режим работы
Понедельник - пятница с *09:00* до *18:00*
Суббота с *10:00* до *16:00*
Воскресенье выходной день ''',parse_mode='Markdown', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Заказать займ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        oner=bot.send_message(chat_id=c.message.chat.id, text='''*Введи сумму от 5000 до 30.000 рублей*''',parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(oner, zaim1)
    elif c.data == '✅Заказать этот займ✅':
        bot.send_message(chat_id=c.message.chat.id, text='''*Заявка оформлена*''', parse_mode='Markdown')
        f = open('{}.txt'.format(c.message.chat.id), 'r')
        line = f.readlines()
        fio = line[2]
        sym = line[0]
        sroci = line[1]
        number = line[3]
        bot.send_message(chat_id='386704067', text='''*{}*
Сумма *{}* рублей 
Срок *{}* дней 
Номер *{}*'''.format(fio, sym, sroci, number), parse_mode='Markdown')
        f.close()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '{}.txt'.format(c.message.chat.id))
        os.remove(path)
    elif c.data == 'Зaказать займ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        rone = bot.send_message(chat_id=c.message.chat.id, text='''*Введи сумму от 100.000 до 5.000.000 рублей*''',
                            parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(rone, dom1)

    elif c.data == 'Закaзать займ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['в меню▶']])
        ronet = bot.send_message(chat_id=c.message.chat.id, text='''*Введи сумму от 50.000 до 1.000.000 рублей*''',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(ronet, car1)
    elif c.data == 'Где мы находимся':
        bot.send_message(chat_id=c.message.chat.id,  text='''Мы находимся по адрессу г. Казань
улица Пушкина дом *12*
офис *203*''', parse_mode='Markdown')
        bot.send_location(chat_id=c.message.chat.id, latitude='55.789027', longitude=' 49.124611')
    elif c.data == 'Документация':
        keyboard = types.InlineKeyboardMarkup()
        abutton = types.InlineKeyboardButton(text="Выписка из списка участников", url='http://creditkzn.com/wp-content/uploads/2016/12/vypiska-iz-spiska-uchastnikov.docx')
        bbutton = types.InlineKeyboardButton(text="Общие условия договора займа от 15.07.2016",
                                                   url='http://creditkzn.com/wp-content/uploads/2016/12/obshchie-usloviya-dogovora-ot-15-07-2016.docx')
        cbutton = types.InlineKeyboardButton(text="ОГРН", url="http://creditkzn.com/wp-content/uploads/2016/12/ogrn.jpg")
        dbutton = types.InlineKeyboardButton(text="Политика в отношении обработки данных", url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%9F%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B2%20%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B8%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.docx")
        fbutton = types.InlineKeyboardButton(text="Информация об условиях от 15.07.2016", url="http://creditkzn.com/wp-content/uploads/2016/12/informaciya-ob-usloviyah-ot-15-07-2016.docx")
        gbutton = types.InlineKeyboardButton(text='Свидетельство "ИНВЕСТ ТРАСТ КОМПАНИ"', url="http://creditkzn.com/wp-content/uploads/2016/12/invest-trast-kompani.jpg")
        ibutton = types.InlineKeyboardButton(text='Антикоррупционная политика МКК ИТК', url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%BE%D1%80%D1%80%D1%83%D0%BF%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0%20%D0%9C%D0%9A%D0%9A%20%D0%98%D0%A2%D0%9A.docx")
        hbutton = types.InlineKeyboardButton(text='Положение о взаимодействии с заемщиками МКК ИТК', url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%9F%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BE%20%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B8%20%D1%81%20%D0%B7%D0%B0%D0%B5%D0%BC%D1%89%D0%B8%D0%BA%D0%B0%D0%BC%D0%B8%20%D0%9C%D0%9A%D0%9A%20%D0%98%D0%A2%D0%9A.docx")
        jbutton = types.InlineKeyboardButton(text='Правило выдачи микрозаймов от 15.07.2016', url="http://creditkzn.com/wp-content/uploads/2016/12/pravila-vydachi-mikrozai-mov-ot-15-07-2016.docx")
        kbutton = types.InlineKeyboardButton(text='Свидетельство МКК', url="http://creditkzn.com/wp-content/uploads/2016/12/svidetelstvo-mkk.jpg")
        lbutton = types.InlineKeyboardButton(text='Базовый стандарт от 22.06.2017', url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%91%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%20%D0%BE%D1%82%2022.06.2017.docx")
        pbutton = types.InlineKeyboardButton(text='Пользовательское соглашение', url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D0%B5.docx")
        obutton = types.InlineKeyboardButton(text='Памятка заемщику', url="http://creditkzn.com/wp-content/uploads/2016/12/pamyatka-zaemshchiku.pdf")
        ubutton = types.InlineKeyboardButton(text='ИНН', url="http://creditkzn.com/wp-content/uploads/2016/12/inn.jpg")
        ybutton = types.InlineKeyboardButton(text='Заявление на реструктуризацию долга', url="http://creditkzn.com/wp-content/uploads/2016/12/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D1%80%D0%B5%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B4%D0%BE%D0%BB%D0%B3%D0%B0.doc")

        keyboard.add(abutton)
        keyboard.add(bbutton)
        keyboard.add(cbutton)
        keyboard.add(dbutton)
        keyboard.add(fbutton)
        keyboard.add(gbutton)
        keyboard.add(ibutton)
        keyboard.add(hbutton)
        keyboard.add(jbutton)
        keyboard.add(kbutton)
        keyboard.add(lbutton)
        keyboard.add(pbutton)
        keyboard.add(obutton)
        keyboard.add(ubutton)
        keyboard.add(ybutton)


        bot.send_message(chat_id=c.message.chat.id,text='*Документация*', parse_mode='Markdown', reply_markup=keyboard)




bot.polling(none_stop=True, interval=4)
