import telebot
from telebot import types

API_TOKEN = '6094386761:AAFPrt-ZYA0XDzR_54ry637EcHRcnc0vEuA'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id,text='Привіт! Вітаємо вас у боті Shaurma Island\nОберіть один з пунктів нижче:')
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("but1")
    kb.add(button1)
    bot.send_message(message.chat.id,"Shaurma island - very well" ,reply_markup=kb)
    with open('stonik.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)
    



bot.polling()
