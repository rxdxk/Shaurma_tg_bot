import telebot
from telebot import types
from keyboards import main_menu_kb,start_kb,order_kb,shaurma_kb,falafel_kb,garniers_kb,rols_kb,drinks_kb
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
   elif message.text == 'Зробити замовлення':
       bot.send_message(message.chat.id,"Ось наші позиції",reply_markup=order_kb)


@bot.callback_query_handler(func = lambda callback:callback.data)
def check_callback_data(callback):
    if callback.data == "Шаурма":
     bot.send_message(callback.message.chat.id,"Це наші шаурми",reply_markup=shaurma_kb)
    elif callback.data == 'Фалафель':
        bot.send_message(callback.message.chat.id,"Це наші фалафелі",reply_markup=falafel_kb)
    elif callback.data == 'Гарніри':
        bot.send_message(callback.message.chat.id,"Це наші фалафелі",reply_markup=garniers_kb)
    elif callback.data == 'Роли':
        bot.send_message(callback.message.chat.id,"Це наші роли",reply_markup=rols_kb)
    elif callback.data == 'Напої':
        bot.send_message(callback.message.chat.id,"Це наші напої",reply_markup=drinks_kb)


    

bot.polling()


    

bot.polling()



