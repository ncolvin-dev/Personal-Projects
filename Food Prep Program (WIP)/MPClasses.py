import tkinter as tk
import mysql.connector
from mysql.connector import errors

class DB:
    def dbconn():
        try:
            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="nickpicachu21", 
                database="dbMealPlanning"
            )
            return conn
        except errors as exception:
            print(f"Error: {exception}")

    def Get_Users_GUI():
        conn = DB.dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        Users = cursor.fetchall()
        cursor.close()
        conn.close()
        return Users




