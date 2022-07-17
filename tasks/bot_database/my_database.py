import mysql.connector

CONNECTED = False

class My_Database:
    def __init__():
        pass
        
    def connect():
        con = mysql.connector.connect()
        if con.is_connected():
            CONNECTED = True
            return con
        else:
            CONNECTED = False
    
    def close_connection(con, cursor):
        con.close()
        cursor.close()

    def get_user_database(id, cursor):
        cursor.execute(f'SELECT id_user FROM users WHERE id_user = {id}')
        userid = cursor.fetchone()
        print(f'User id do get_user: {userid[0]}')
        return userid[0]


    def coins_update_database(cursor, id_user, coins_to_be_added):
        coins_before = cursor.execute(f'SELECT coins_user FROM users WHERE id_user = {id_user}')

        if coins_before == None:
            coins_before = 0
        
        coins_now = coins_before + coins_to_be_added

        cursor.execute(f'UPDATE users SET u')