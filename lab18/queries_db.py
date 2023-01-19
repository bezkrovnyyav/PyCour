import sqlite3


db = sqlite3.connect('blog_db.db')
cursor = db.cursor()
"""
result = cursor.executescript('''
SELECT p.id, p.title, p.content, (SELECT COUNT(*) FROM photos WHERE p.id = photos.post_id) AS num_photos
FROM posts AS p;
''').fetchall()
pprint(result)

"""
with open("db_queries.sql","r") as f:
    for row in f.readlines():
        result = cursor.execute(row).fetchall()
        if result != []:
            print(*result,sep='\n', end='\n'*2)



db.close()
print("Соединение с SQLite закрыто")
