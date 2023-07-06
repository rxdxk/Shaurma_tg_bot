import sqlite3

def base():
  conn = sqlite3.connect('mydatabase.db')

  conn.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT,
                  last_name TEXT,
                  number INTEGER,
                  address TEXT)''')


  conn.execute("INSERT INTO orders (first_name, last_name, order_number, address) VALUES (?, ?, ?, ?)",
             (user_data, basket, user_num, user_adress))

  conn.commit()

  cursor = conn.execute("SELECT * FROM orders")
  for row in cursor:
      print(row)

  conn.close()
