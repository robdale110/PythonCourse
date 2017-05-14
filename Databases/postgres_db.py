import psycopg2

def create_table():
    connection = psycopg2.connect("dbname='test_db' user='postgres' password='r0bL973' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='test_db' user='postgres' password='r0bL973' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Store VALUES(%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='test_db' user='postgres' password='r0bL973' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Store")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname='test_db' user='postgres' password='r0bL973' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Store WHERE item = %s", (item,))
    connection.commit()
    connection.close()

def update(item, quantity, price):
    connection = psycopg2.connect("dbname='test_db' user='postgres' password='r0bL973' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("UPDATE Store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    connection.commit()
    connection.close()

create_table()
#insert("Apple", 10, 7)
#insert("Orange", 10, 7)
#delete("Orange")
update("Apple", 20, 12)
print(view())