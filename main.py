import os
import telebot
#Импорт базы данных
import db
#Импорты клавиатур из  keyboaards.py
from keyboards import * 
#Загрузка .env
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN') #Токен из .env
bot = telebot.TeleBot(API_TOKEN) 

my_dict = {}

def send_photo(path,message):
          with open(path,'rb') as file:
           bot.send_photo(message.chat.id,file)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Для того щоб подивитьсь меню натисніть:меню\nщоб оформити замовлення натисныть оформити замовлення")

@bot.message_handler(commands=['start'])  #Приветствие
def say_hello(message):
    user_id = message.from_user.id
    if user_id not in my_dict:
        my_dict[user_id] = []
    send_photo('stonik.jpg',message)
    bot.send_message(message.chat.id,"Shaurma island - very well" ,reply_markup=start_kb)
    bot.send_message(message.chat.id,'Привіт! Вітаємо вас у боті Shaurma Island\nОберіть один з пунктів нижче:',reply_markup = main_menu_kb)

@bot.message_handler() #Основной хендлер
def kb_answer(message):
   
   def get_user_adress(message): #Адрес пользователя
       msg = bot.send_message(message.chat.id,'Напишіть вашу адресу')
       bot.register_next_step_handler(msg,get_user_adress_next_step)

   def get_user_adress_next_step(message): #Адрес пользователя2
       global user_adres
       user_adress = message.text
       bot.send_message(message.chat.id,"Ваше замовлення прийнято")
       my_dict.clear()
       db.create_order(user_data, str(basket), user_num, user_adress)

   def check_user_num(message):   #Проверка номера 1
       msg = bot.send_message(message.chat.id,'Напишіть номер телефону почнаючи з 0',reply_markup=types.ReplyKeyboardRemove())
       bot.register_next_step_handler(msg,check_user_num_next_step)

   def check_user_num_next_step(message): #Проверка номера 2
        global user_num
        user_num = message.text
        if len(user_num) == 10 and user_num[0] == '0':
            bot.send_message(message.chat.id,f'Ваш номер {user_num}')
            get_user_data(message)
        elif len(user_num) != 10 or user_num[0] != '0':
            bot.send_message(message.chat.id,'Номер введено невірно')
            check_user_num(message)

   def get_user_data(message): #Получаем имя и фамилию 1
       msg = bot.send_message(message.chat.id,"Введіть ваше ім'я та призвище")
       bot.register_next_step_handler(msg,get_user_data_next_step)

   def get_user_data_next_step(message):#Получаем имя и фамилию 1
       global user_data
       user_data = message.text
       bot.send_message(message.chat.id,f"Ваше ім'я та прізвище:{user_data}")
       get_user_adress(message)

   def acception_key_func(acception_buttons): #Генерация клавиатуры при отказе от чего-то в заказе
    for x in basket:
      acception_buttons.append(types.KeyboardButton(x))

   def user_order_acception(message): #Принятие заказа да/нет 1
       msg = bot.send_message(message.chat.id,f"Все вірно ?",reply_markup=yes_or_no_kb)
       show_basket()
       bot.register_next_step_handler(msg,user_order_acception_next_step)

   def user_order_acception_next_step(message): #Принятие заказа да/нет 1
       user_response = message.text
       if user_response == 'Так' and basket != []:
           bot.send_message(message.chat.id,"Супер!")
           check_user_num(message)
       elif user_response =='Так' and basket ==[]:
           bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)
       elif user_response == "Ні" and basket != []:
           acception_buttons = []
           acception_key_func(acception_buttons)
           acception_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*acception_buttons)
           msg = bot.send_message(message.chat.id,"Що ви хочете змінити ?",reply_markup=acception_kb)
           bot.register_next_step_handler(msg,user_order_acception_forward)
       elif user_response == "Ні" and basket == []:
           bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)

   def user_order_acception_forward(message): #Принятие заказа да/нет + клавиатура 
    if basket != []:
       user_acception = message.text
       basket.remove(message.text)
       user_order_acception(message)
    else:
        bot.send_message(message.chat.id,"Ваша корзина пуста (",reply_markup=main_menu_kb)

   def basket_append(message):
     user_id = message.from_user.id
     my_dict[user_id].append(message.text)
     bot.reply_to(message, f"Товар {message.text} доданий в корзину")
     print(my_dict)

   def show_basket():#Показывает корзину 
       global basket
       user_id = message.from_user.id
       basket = my_dict[user_id]
       basket_str = (', ').join(basket)
       bot.reply_to(message, f"Ваша корзина: {basket_str}")

   if message.text == 'Меню':  #При нажатии Меню
       bot.send_message(message.chat.id,"Ось нaше меню:")
       send_photo('menu.jpg',message)
   elif message.text == 'Назад': #При нажатии Назад
           bot.send_message(message.chat.id,"Ви повернулись назад",reply_markup=main_menu_kb)
   elif message.text == "Завершити замовленя" and basket != []: #При нажатии Завершить если корзина не пустая
       show_basket()
       user_order_acception(message)
   elif message.text == "Завершити замовленя" and basket == []: #При нажатии Завершить если корзина пустая
       bot.send_message(message.chat.id, "Ваше замовлення пусте(")
       print(basket)
   elif message.text == 'Оформити замовлення': #При нажати Зробити замовлення
       bot.send_message(message.chat.id,"Ось наші позиції,щоб вибрати натисніть на кнопку",reply_markup=order_kb)   
    #Проверки на фильтрацию слова Завершить заказ дабы оно не попадало в корзину как елемент
   elif message.text  in shaurma_posititons[0:7]:
      basket_append(message)
      show_basket()
   elif message.text  in falafel_positions[0:2]:
       basket_append(message)
       show_basket()
   elif message.text  in rols_positions[0:5]:
       basket_append(message)
       show_basket()
   elif message.text  in drinks_positions[0:3]:
       basket_append(message)
       show_basket()
   elif message.text  in dodatki_positions[0:6]:
      basket_append(message)
      show_basket()
   elif message.text in garniers_positions[0:3]:
        basket_append(message)
        show_basket()
   else:
       bot.send_message(message.chat.id,"Я вас не розумію(")

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

