"""Blog
Create the scheme for the Personal Blog. Create the Database, tables, views(at least 1).
Add constraints, indexes. Add the field for saving photos/files for each blog's post.
Note: Use any RDBMS that you want. Use at least 4 tables.
Bonus task: fill the tables with the data from csv files
"""

import sqlite3


db = sqlite3.connect('blog_db.db')
cursor = db.cursor()
print("База данных создана и успешно подключена к SQLite")

with open("schema.sql","r") as f:
    cursor.executescript(f.read())
    db.commit()
print("Таблицы SQLite созданы")
db.close()
print("Соединение с SQLite закрыто")
