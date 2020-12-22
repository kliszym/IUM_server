import sqlite3
import db_functions
import random


class DbConnection:

    db_products = 'warehouse.db'

    conn = None
    c = None

    @staticmethod
    def connect():
        DbConnection.conn = sqlite3.connect(DbConnection.db_products)
        DbConnection.c = DbConnection.conn.cursor()

    @staticmethod
    def disconnect():
        DbConnection.conn.commit()
        DbConnection.conn.close()

    @staticmethod
    def get_content():
        DbConnection.connect()
        DbConnection.c.execute(db_functions.GET_ALL)
        result = {"result": [dict((DbConnection.c.description[i][0], quantity)
                  for i, quantity in enumerate(row)) for row in DbConnection.c.fetchall()]
                  }
        DbConnection.disconnect()
        return result

    @staticmethod
    def update_content(data):
        DbConnection.connect()
        for content in data:
            try:
                DbConnection.c.execute(db_functions.UPDATE,
                    (content['manufacturer'], content['model'], content['price'], content['obj_id']))
            except:
                continue
        DbConnection.disconnect()

    @staticmethod
    def create_unique_id():
        maybe_unique_id = ''
        while True:
            maybe_unique_id = ''
            for i in range(6):
                maybe_unique_id += str(random.randint(0, 10))
            DbConnection.connect()
            DbConnection.c.execute(db_functions.GET_ALL_ID)
            all_ids = DbConnection.c.fetchall()
            if maybe_unique_id not in all_ids:
                break
        return maybe_unique_id

    @staticmethod
    def create_product(data):
        result = []
        DbConnection.connect()
        for content in data:
            try:
                unique_id = DbConnection.create_unique_id()
                DbConnection.c.execute(db_functions.ADD,
                    (unique_id, content['manufacturer'], content['model'], content['price'], 0))
                result.append({"c_id": content["obj_id"], "s_id": unique_id})
            except Exception as e:
                print(e)
                continue
        DbConnection.disconnect()
        return result

    @staticmethod
    def increase(data):
        DbConnection.connect()
        for content in data:
            try:
                DbConnection.c.execute(db_functions.GET_QUANTITY, (content['obj_id'],))
                quantity = DbConnection.c.fetchall()[0][0]
                quantity += content['quantity']
                DbConnection.c.execute(db_functions.SET_QUANTITY, (quantity, content['obj_id']))
            except Exception as e:
                print(e)
                continue
        DbConnection.disconnect()

    @staticmethod
    def decrease(data):
        DbConnection.connect()
        for content in data:
            try:
                DbConnection.c.execute(db_functions.GET_QUANTITY, (content['obj_id'],))
                quantity = DbConnection.c.fetchall()[0][0]
                quantity -= content['quantity']
                if quantity < 0:
                    continue
                DbConnection.c.execute(db_functions.SET_QUANTITY, (quantity, content['obj_id']))
            except Exception as e:
                print(e)
                continue
        DbConnection.disconnect()

    @staticmethod
    def remove_product(data):
        DbConnection.connect()
        for content in data:
            try:
                DbConnection.c.execute(db_functions.REMOVE, (content['obj_id'],))
            except:
                continue
        DbConnection.disconnect()

    @staticmethod
    def get_user(user):
        DbConnection.connect()
        DbConnection.c.execute(db_functions.GET_USER, (user,))
        result = DbConnection.c.fetchall()
        DbConnection.disconnect()
        return result
