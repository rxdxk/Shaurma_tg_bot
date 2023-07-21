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
    cursor.close()
    conn.close()
