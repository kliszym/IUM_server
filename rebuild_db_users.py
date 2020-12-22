import sqlite3


conn = sqlite3.connect('warehouse.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS users')
c.execute('''CREATE TABLE users (
            username text NOT NULL UNIQUE,
            password text NOT NULL,
            master boolean NOT NULL
          );''')

users = [('worker', 'worker1', False, ),
         ('master', 'master1', True),
         ]

c.executemany('INSERT INTO users VALUES (?,?,?)', users)

conn.commit()
conn.close()
