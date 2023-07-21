import sqlite3
group_chat_id=-922258463

def create_order(user_data, basket_str, user_num, user_adress):
    conn = sqlite3.connect('zxc.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            user_data TEXT,
            basket_str TEXT,
            user_num INTEGER,
            user_adress TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO orders (user_data, basket_str, user_num, user_adress)
        VALUES (?, ?, ?, ?)
    ''', (user_data, basket_str, user_num, user_adress,))

    # Выполнение запроса для получения новых элементов из таблицы
    cursor.execute('SELECT * FROM orders WHERE sent = 0')
    new_rows = cursor.fetchall()

    # Отправка новых элементов в группу
    for row in new_rows:
        user_data, basket_str, user_num, user_adress = row[0], row[1], row[2], row[3]
        message = f"Нове замовлення: Данні: {user_data}, Замовлення: {basket_str}, Номер телефону:{user_num}, Адресса:{user_adress} "
        bot.send_message(group_chat_id, message)

        # Помечаем элемент как отправленный, чтобы не отправить его снова в будущем
        cursor.execute('UPDATE orders SET sent = 1 WHERE user_data = ?, basket_str = ?, user_num = ?, user_adress = ?', (user_data, basket_str, user_num, user_adress,))
        conn.commit()

    # Закрытие курсора и подключения
    cursor.close()
    conn.close()
