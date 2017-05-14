import sqlite3

def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Store")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Store WHERE item = ?", (item,))
    connection.commit()
    connection.close()

def update(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    connection.commit()
    connection.close()

#insert("Coffee Cup", 10, 7)
#delete("Wine Glass")
update("Water glass", 20, 12)
print(view())