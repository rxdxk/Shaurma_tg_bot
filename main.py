import telebot
from telebot import types
from keyboards import main_menu_kb,food_menu_kb,start_kb

food_menu = False

API_TOKEN = '6094386761:AAFPrt-ZYA0XDzR_54ry637EcHRcnc0vEuA'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def say_hello(message):
    with open('stonik.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)
    bot.send_message(message.chat.id,"Shaurma island - very well" ,reply_markup=start_kb)
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id,'Привіт! Вітаємо вас у боті Shaurma Island\nОберіть один з пунктів нижче:',reply_markup = main_menu_kb)
  




@bot.message_handler()
def kb_answer(message):
   if message.text == 'Контакти':
       bot.send_message(message.chat.id,"+123456789")
    
   elif message.text == 'Меню':
       bot.send_message(message.chat.id,"Ось наше меню:",reply_markup=food_menu_kb)
       global food_menu
       food_menu = True
   elif message.text == 'Назад':
       if food_menu == True:
           bot.send_message(message.chat.id,"Ви повернулись назад",reply_markup=main_menu_kb)
    

    

bot.polling()


