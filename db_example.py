import sqlite3

def create_order(user_data, basket, user_num, user_adress):
    conn = sqlite3.connect('asd.db')


    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            user_data TEXT,
            basket TEXT,
            user_num INTEGER,
            user_adress TEXT
        )
    ''')

  
    cursor.execute('''
        INSERT INTO orders (user_data, basket, user_num, user_adress)
        VALUES (?, ?, ?, ?)
    ''', (user_data, basket, user_num, user_adress,))


    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    cursor.close()
    conn.close()
