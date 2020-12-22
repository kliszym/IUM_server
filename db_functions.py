GET_ALL = 'SELECT obj_id, manufacturer,model,price,quantity FROM product_info'
GET_USER = 'SELECT * FROM users WHERE username == ?'
UPDATE = '''UPDATE product_info
            SET manufacturer = ?, model = ?, price = ?
            WHERE obj_id == ?'''
ADD = '''INSERT INTO product_info VALUES (?, ?, ?, ?, ?)'''
REMOVE = '''DELETE FROM product_info WHERE obj_id == ?'''
GET_QUANTITY = '''SELECT quantity FROM product_info WHERE obj_id == ?'''
SET_QUANTITY = '''UPDATE product_info
                    SET quantity = ?
                    WHERE obj_id == ?'''
GET_ALL_ID = '''SELECT obj_id FROM product_info'''
