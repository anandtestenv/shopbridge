import sqlite3

# Get connecting of shopbridge db
conn = sqlite3.connect('shopbridge.db')

#Create Table
conn.execute('CREATE TABLE products(pid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,description TEXT NOT NULL,price INTEGER,quantity INTEGER)')
print('Table created')
#commit changes
conn.commit()
#close connection
conn.close()