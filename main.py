import telebot
import database
import os 
from telebot import types
#Импорты клавиатур из  keyboaards.py
from keyboards import *
#Загрузка .env
from dotenv import load_dotenv


load_dotenv()


API_TOKEN = os.getenv('API_TOKEN') #Токен из .env
bot = telebot.TeleBot(API_TOKEN) 


basket =  [] #Общая корзина товаров 


@bot.message_handler(commands=['start'])  #Приветствие
def say_hello(message):
    with open('stonik.jpg','rb') as file:
        bot.send_photo(message.chat.id,file)
    bot.send_message(message.chat.id,"Shaurma island - very well" ,reply_markup=start_kb)
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id,'Привіт! Вітаємо вас у боті Shaurma Island\nОберіть один з пунктів нижче:',reply_markup = main_menu_kb)


@bot.message_handler() #Основной хендлер
def kb_answer(message):  
   

   def check_num(message):   #Проверка номера 1
       msg = bot.send_message(message.chat.id,'Напишіть номер телефону у форматі 0123456789')
       bot.register_next_step_handler(msg,check_num2)
   def check_num2(message): #Проверка номера 2
        user_num = message.text
        if len(user_num) == 10 and user_num[0] == '0':
            bot.send_message(message.chat.id,f'Ваш номер {user_num}')
            get_user_data(message)
        elif len(user_num) != 10 or user_num[0] != '0':
            bot.send_message(message.chat.id,'Номер введено невірно')
            check_num(message)


   def get_user_data(message): #Получаем имя и фамилию 1
       msg = bot.send_message(message.chat.id,"Введіть ваше ім'я та призвище")
       bot.register_next_step_handler(msg,get_user_data2)
   def get_user_data2(message):#Получаем имя и фамилию 1
       user_data = message.text
       bot.send_message(message.chat.id,f"Ваше ім'я та прізвище:{user_data}")
       bot.send_message(message.chat.id,"Ваше замовлення прийнято")


   def order_acception(message): #Принятие заказа да/нет 1
       msg = bot.send_message(message.chat.id,f"Все вірно ?",reply_markup=yes_or_no_kb)
       show_basket()
       bot.register_next_step_handler(msg,order_acception2)
   def acception_key_func(acception_buttons): #Генерация клавиатуры при отказе от чего-то в заказе
    for x in basket:
      acception_buttons.append(types.KeyboardButton(x))
   def order_acception2(message): #Принятие заказа да/нет 1
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


   def order_acception3(message): #Принятие заказа да/нет + клавиатура 
    if basket != []:
       user_acception = message.text
       basket.remove(message.text)
       order_acception(message)
    else:
        bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)


   def show_basket(): #Показывает корзину 
    basket_str = (', ').join(basket)
    bot.send_message(message.chat.id,f"Ваша корзина:{basket_str}")


   if message.text == 'Меню':  #При нажатии Меню
       with open('menu.jpg','rb') as file:
           bot.send_message(message.chat.id,"Ось нaше меню:")
           bot.send_photo(message.chat.id,file)

    
   if message.text == 'Назад': #При нажатии Назад
           bot.send_message(message.chat.id,"Ви повернулись назад",reply_markup=main_menu_kb)

    
   if message.text == "Завершити замовленя" and basket != []: #При нажатии Завершить если корзина не пустая
       show_basket()
       order_acception(message)
       database.base()

    
   if message.text == "Завершити замовленя" and basket == []: #При нажатии Завершить если корзина пустая
       bot.send_message(message.chat.id, "Ваше замовлення пусте(")
   if message.text == 'Зробити замовлення': #При нажати Зробити замовлення
       bot.send_message(message.chat.id,"Ось наші позиції,щоб вибрати натисніть на кнопку",reply_markup=order_kb)
       
    
    #Проверки на фильтрацию слова Завершить заказ дабы оно не попадало в корзину как елемент
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
      

@bot.callback_query_handler(func = lambda callback:callback.data) #Хендлер инлайн клавиатуры заказа
def check_callback_data(callback):
    #Инструкции callback даты с той же клавиатуры
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


#Запуск
bot.polling()


#Запуск
bot.polling()
