# бот должен составлять предсказание на сегоднящний день
import telebot
from telebot import types
import random

bot = telebot.TeleBot('1067406680:AAFUcDdxkI21NIwBwktFJIyWFI24cAkuZCM')

firstPartOfSentence = ["Сегодня прекрасный день для того, чтобы открыть для себя что-то новое.\n",
                       "Звезды сегодня благосколнно влияют на Вашу удачу.\n",
                       "Будьте осторожны, сегодняшний день предвещает беду.\n"]

secondParOfSentence = ["Но помните, что даже в этом случае нужно не забывать про",
                       "Если поедете за город, заранее подумайте про",
                       "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
                       "Если у вас упадок сил, обратите внимание на",
                       "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

secondParOfSentencePlus = ["отношения с друзьями и близкими.\n",
                           " работу и деловые вопросы, которые могут так некстати помешать планам.\n",
                           "себя и своё здоровье, иначе к вечеру возможен полный раздрай.\n",
                           "бытовые вопросы — особенно те, которые вы не доделали вчера.\n",
                           "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца.\n"]

thirdParOfSentence = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.\n",
                      "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.\n",
                      "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.\n",
                      "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.\n",
                      "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты.\n"]


@bot.message_handler(content_types=['text'])
def getTextMessage(messege):
    if messege.text.lower() == "привет" or messege.text == "/start":
        bot.send_message(messege.from_user.id, "Приветусики, сейчас погадаю тебе, как моя бабка меня учила")
        keyboard = types.InlineKeyboardMarkup()
        keyOven = types.InlineKeyboardButton(text='Овен', callback_data = 'zodiac')
        keyboard.add(keyOven)
        keyTelec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(keyTelec)
        keyBliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(keyBliznecy)
        keyRak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(keyRak)
        keyLev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(keyLev)
        keyDeva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(keyDeva)
        keyVesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(keyVesy)
        keySkorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(keySkorpion)
        keyStrelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(keyStrelec)
        keyKozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(keyKozerog)
        keyVodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(keyVodoley)
        keyRybi = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(keyRybi)
        bot.send_message(messege.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif messege.text == "/help":
        bot.send_message(messege.from_user.id, "Напиши Привет")
    else:
        bot.send_message(messege.from_user.id, "Твоя моя не понимать, сорямба. Напиши /help")

@bot.callback_query_handler(func=lambda call: True)
def callback_woeker(call):
    if call.data == "zodiac":
        message = random.choice(firstPartOfSentence) + ' ' + random.choice(secondParOfSentence) + ' ' + random.choice(
            secondParOfSentencePlus) + ' ' + random.choice(thirdParOfSentence)
        bot.send_message(call.message.chat.id, message)


bot.polling(none_stop=True, interval=0)
