 import sqlite3

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
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall() 
    for row in rows:
        with open('zxc.txt', w) as file:
            file.write(str(rows))
    # Создание подключения к базе данных
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Выполнение запроса для получения новых элементов из таблицы
    cursor.execute('SELECT * FROM orders WHERE sent = 0')
    new_rows = cursor.fetchall()

    # Отправка новых элементов в группу
    for row in new_rows:
        order_id, name = row[0], row[1]
        message = f"Новый заказ: Order ID: {order_id}, Name: {name}"
        bot.send_message(group_chat_id, message)

        # Помечаем элемент как отправленный, чтобы не отправить его снова в будущем
        cursor.execute('UPDATE orders SET sent = 1 WHERE order_id = ?', (order_id,))
        conn.commit()

    # Закрытие курсора и подключения
    cursor.close()
    conn.close()
