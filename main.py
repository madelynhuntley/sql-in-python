from email.headerregistry import Address
import sqlite3

connection = sqlite3.connect('dp_customers copy.db')

cursor = connection.cursor()

# rows = cursor.execute("SELECT name, city, state, postal_code FROM Customers ORDER BY name ").fetchall();

# print(rows)
# columns = ['Name', 'City', 'State', 'ZIP Code']
# print(f'{columns[0]:<25} {columns[1]:27} {columns[2]:<10} {columns[3]}')


# for row in rows:
#    print(f'{row[0]:<25} {row[1]:<27} {row[2]:<10} {row[3]}')

# update_sql = ("UPDATE Customers SET city=?, state=? WHERE customer_id=? OR customer_id = ? OR customer_id = ? OR customer_id=?")
# update_vals = ('Dallas','TX','1','2','3','4')
# cursor.execute(update_sql,update_vals)

# connection.commit()
insert_sql = "INSERT INTO Customers(name, street_address, city, state, postal_code) VALUES(?,?,?,?,?)"
for customer in range(15):
    name = input('Enter your name:')
    address = input('Enter address:')
    city = input('Enter city:')
    state = input('Enter a state:')
    zip = input('Enter a zip code:')
    values = (name,address, city, state, zip)
    cursor.execute(insert_sql,values)
connection.commit()