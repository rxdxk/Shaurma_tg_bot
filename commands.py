from config import bot,my_dict
from keyboards import main_menu_kb,start_kb
from send_photo_func import send_photo


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
    