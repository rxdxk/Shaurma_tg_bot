import telebot
from telebot import types
from keyboards import main_menu_kb,start_kb,order_kb,shaurma_kb,falafel_kb,garniers_kb,rols_kb,drinks_kb,shaurma_posititons,rols_positions,drinks_positions,falafel_positions,garniers_positions,yes_or_no_kb,dodatki_kb,dodatki_positions
import os 
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

global basket 
basket =  []
global basket_str
basket_str = ''
user_adres = ''
global func_reply
func_reply = False

@bot.message_handler(commands=['start'])
def say_hello(message):
    with open('stonik.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)
    bot.send_message(message.chat.id,"Shaurma island - very well" ,reply_markup=start_kb)
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id,'Привіт! Вітаємо вас у боті Shaurma Island\nОберіть один з пунктів нижче:',reply_markup = main_menu_kb)



@bot.message_handler()
def kb_answer(message):
   def check_num(message):
       msg = bot.send_message(message.chat.id,'Напишіть номер телефону у форматі 0123456789')
       bot.register_next_step_handler(msg,check_num2)
   def check_num2(message):
        user_num = message.text
        if len(user_num) == 10 and user_num[0] == '0':
            bot.send_message(message.chat.id,f'Ваш номер {user_num}')
            get_user_data(message)
        elif len(user_num) != 10 or user_num[0] != '0':
            bot.send_message(message.chat.id,'Номер введено невірно')
            check_num(message)
   def get_user_data(message):
       msg = bot.send_message(message.chat.id,"Введіть ваше ім'я та призвище")
       bot.register_next_step_handler(msg,get_user_data2)
   def get_user_data2(message):
       user_data = message.text
       bot.send_message(message.chat.id,f"Ваше ім'я та прізвище:{user_data}")
   def order_acception(message):
       msg = bot.send_message(message.chat.id,f"Все вірно ?",reply_markup=yes_or_no_kb)
       show_basket()
       bot.register_next_step_handler(msg,order_acception2)
   def acception_key_func(acception_buttons):
    for x in basket:
      acception_buttons.append(types.KeyboardButton(x))
   def order_acception2(message):
       user_response = message.text
       if user_response == 'Так' and basket != []:
           bot.send_message(message.chat.id,"Супер!")
           check_num(message)
       elif user_response =='Так' and basket ==[]:
           bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)
       elif user_response == "Ні" and basket != []:
           acception_buttons = []
           acception_key_func(acception_buttons)
           acception_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*acception_buttons)
           msg = bot.send_message(message.chat.id,"Що ви хочете змінити ?",reply_markup=acception_kb)
           bot.register_next_step_handler(msg,order_acception3)
       elif user_response == "Ні" and basket == []:
           bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)

   def order_acception3(message):
    if basket != []:
       user_acception = message.text
       basket.remove(message.text)
       order_acception(message)
    else:
        bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)


   def show_basket():
    basket_str = (', ').join(basket)
    bot.send_message(message.chat.id,f"Ваша корзина:{basket_str}")
   if message.text == 'Меню':
       with open('menu.jpg','rb') as file:
           bot.send_message(message.chat.id,"Ось нaше меню:")
           bot.send_photo(message.chat.id,file)
   if message.text == 'Назад':
           bot.send_message(message.chat.id,"Ви повернулись назад",reply_markup=main_menu_kb)
   if message.text == "Завершити замовленя" and basket != []:
       show_basket()
       order_acception(message)
   if message.text == "Завершити замовленя" and basket == []:
       bot.send_message(message.chat.id, "Ваше замовлення пусте(")
   if message.text == 'Зробити замовлення':
       bot.send_message(message.chat.id,"Ось наші позиції,щоб вибрати натисніть на кнопку",reply_markup=order_kb)
   if message.text  in shaurma_posititons[0:7]:
      basket.append(message.text)
      show_basket()
   if message.text  in falafel_positions[0:2]:
       basket.append(message.text)
       show_basket()
   if message.text  in rols_positions[0:5]:
       basket.append(message.text)
       show_basket()
   if message.text  in drinks_positions[0:3]:
       basket.append(message.text)
       show_basket()
   if message.text  in dodatki_positions[0:5]:
      basket.append(message.text)
      show_basket()
      
@bot.callback_query_handler(func = lambda callback:callback.data)
def check_callback_data(callback):
    if callback.data == "Шаурма":
     bot.send_message(callback.message.chat.id,"Це наші шаурми",reply_markup=shaurma_kb)
    if callback.data == 'Фалафель':
        bot.send_message(callback.message.chat.id,"Це наші фалафелі",reply_markup=falafel_kb)
    if callback.data == 'Гарніри':
        bot.send_message(callback.message.chat.id,"Це наші фалафелі",reply_markup=garniers_kb)
    if callback.data == 'Роли':
        bot.send_message(callback.message.chat.id,"Це наші роли",reply_markup=rols_kb)
    if callback.data == 'Напої':
        bot.send_message(callback.message.chat.id,"Це наші напої",reply_markup=drinks_kb)
    if callback.data == 'Додатки':
        bot.send_message(callback.message.chat.id,"Це наші додатки",reply_markup=dodatki_kb)



  




  

  
bot.polling()


