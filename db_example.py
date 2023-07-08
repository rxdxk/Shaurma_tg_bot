import sqlite3

def create_order(order_id):
    conn = sqlite3.connect('asd.db')


    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER,
            name TEXT
        )
    ''')

  
    name = input("Введіть ваше ім'я: ")

  
    cursor.execute('''
        INSERT INTO orders (order_id, name)
        VALUES (?, ?)
    ''', (order_id, name,))


    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    cursor.close()
    conn.close()


order_id = int(input("Введіть ID замовлення: "))

create_order(order_id)
