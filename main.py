from telebot import TeleBot
from config import bot
from handlers import commands,message,callback



#Запуск
if __name__ == "__main__":
    bot.polling()

