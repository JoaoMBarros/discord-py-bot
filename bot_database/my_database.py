#Adding the directory to the sys path so I can import it
import repackage
repackage.up()

import mysql.connector

CONNECTED = False

class My_Database:
    def __init__(self):
        pass
        
    #Connect to the database
    def connect():
        con = mysql.connector.connect()
        if con.is_connected():
            CONNECTED = True
            return con
        else:
            CONNECTED = False

    #Get the user id from the database or initialize a new user in case they don't exist
    def get_user(con, cursor, id):
        sql_select = f'SELECT id_user FROM users WHERE id_user = {id}'
        sql_insert = f'INSERT INTO users(id_user, coins_user, bingo_victories) VALUES ({id}, 0, 0)'

        cursor.execute(sql_select)
        userid = cursor.fetchone()

        if userid == None:
            cursor.execute(sql_insert)
            con.commit()
            cursor.execute(sql_select)
            userid = cursor.fetchone()
        
        return userid[0] #The return value from the database is a tuple
    
    def get_user_coins(cursor, id_user):
        #Get the user current coins from the database so I can make sure the update worked
        cursor.execute(f'SELECT coins_user FROM users WHERE id_user = {id_user}')
        coins_now = cursor.fetchone()
        return coins_now[0]
    
    def get_user_bingo_victories(cursor, id_user):
        cursor.execute(f'SELECT bingo_victories FROM users WHERE id_user = {id_user}')
        victories = cursor.fetchone()
        return victories[0]

    #Update the user coins in the database
    def coins_update_database(con, cursor, id_user, coins_to_be_added):
        #Get the user current coins
        cursor.execute(f'SELECT coins_user FROM users WHERE id_user = {id_user}')
        coins = cursor.fetchone()

        #Commit the update to the dabatase
        coins_now = coins + coins_to_be_added
        cursor.execute(f'Update users SET coins_user = {coins_now} WHERE id_user = {id_user}')
        con.commit()