import sqlite3


conn = sqlite3.connect('warehouse.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS product_info')
c.execute('''CREATE TABLE product_info (
          obj_id text NOT NULL UNIQUE,
          manufacturer text NOT NULL,
          model text NOT NULL,
          price double,
          quantity integer
          );''')

products = [('000001', 'Samsung', 'Galaxy S20', 209.99, 8),
            ('000002', 'Samsung', 'Galaxy Note20', 549.99, 19),
            ('000003', 'Samsung', 'Galaxy Z', 999.99, 24),
            ('000004', 'Samsung', 'Galaxy Note10', 664.99, 97),
            ('000005', 'Samsung', 'Galaxy Z Flip', 889.99, 9),
            ('000006', 'Samsung', 'Galaxy S10+', 564.99, 6),
            ('000007', 'Samsung', 'Galaxy S10e', 314.99, 12),
            ('000008', 'Samsung', 'Galaxy XCover Pro', 499.99, 14),
            ('000009', 'Samsung', 'Galaxy A71', 139.99, 38),
            ('000010', 'Samsung', 'Galaxy A51', 164.99, 83),
            ('000011', 'Samsung', 'Galaxy A50', 174.99, 1),
            ]

c.executemany('INSERT INTO product_info VALUES (?,?,?,?,?)', products)

conn.commit()
conn.close()
