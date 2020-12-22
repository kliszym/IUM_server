import db_connection
from sessions import Sessions


def login(credentials):
    print(credentials)
    db_credentials = db_connection.DbConnection.get_user(credentials['username'])
    _, db_password, master = db_credentials[0]
    if credentials['password'] == db_password:
        user_id = Sessions.get_id(master)
        return True, master, user_id
    return False
