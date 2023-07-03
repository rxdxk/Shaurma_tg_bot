import telebot
from telebot import types
from keyboards import main_menu_kb,start_kb
import os 
from dotenv import load_dotenv
 
load_dotenv()
food_menu = False

API_TOKEN = os.getenv('API_TOKEN')
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
    
   if message.text == 'Меню':
       with open('menu.jpg','rb') as file:
           bot.send_message(message.chat.id,"Ось нaше меню:")
           bot.send_photo(message.chat.id,file)
       global food_menu
       food_menu = True
   elif message.text == 'Назад':
       if food_menu == True:
           bot.send_message(message.chat.id,"Ви повернулись назад",reply_markup=main_menu_kb)
    

    

bot.polling()



