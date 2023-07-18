import os
from telebot import TeleBot
#Импорт базы данных
import db
#Импорты клавиатур из  keyboaards.py
from keyboards import * 
#Загрузка .env
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN') #Токен из .env
bot = TeleBot(API_TOKEN) 

my_dict = {}





