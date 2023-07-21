import sqlite3
import os
from telebot import TeleBot
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = TeleBot(API_TOKEN) 
group_chat_id=your_chat_id

def create_order(user_data, basket_str, user_num, user_adress, sent,):
    conn = sqlite3.connect('name.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            user_data TEXT,
            basket_str TEXT,
            user_num INTEGER,
            user_adress TEXT,
            sent INTEGER
        )
    ''')
    cursor.execute('''
        INSERT INTO orders (user_data, basket_str, user_num, user_adress, sent)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_data, basket_str, user_num, user_adress, sent, ))

    # Выполнение запроса для получения новых элементов из таблицы
    cursor.execute('SELECT * FROM orders WHERE sent = 0')
    new_rows = cursor.fetchall()

    # Отправка новых элементов в группу
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    for row in new_rows:
        user_data, basket_str, user_num, user_adress = row[0], row[1], row[2], row[3]
        message = f"Нове замовлення: Данні: {user_data}, Замовлення: {basket_str}, Номер телефону:{user_num}, Адресса:{user_adress} "
        bot.send_message(group_chat_id, message)

        # Помечаем элемент как отправленный, чтобы не отправить его снова в будущем
        cursor.execute('UPDATE orders SET sent = 1 WHERE user_data = ?', (user_data,))
        conn.commit()

    # Закрытие курсора и подключения
    cursor.close()
    conn.close()
