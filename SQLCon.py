import sqlite3
from sqlite3 import Error
from secrets import connection_data
# mycursor.execute("SELECT * FROM accounts")
# myresult = mycursor.fetchall()

class SQLCon():
    
    def __init__(self):
        try:
            self.conn = sqlite3.connect('password_db.db')
            self.mycursor = self.conn.cursor() 
            self.mycursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            website_name text NOT NULL,
                                            user_account text,
                                            user_password text,
                                            pass_key text
                                        );''')
            self.conn.commit()
        except Exception as e:
                print(e)                

    def write_account(self, account_info):
        try:
            sql = "INSERT INTO accounts VALUES (null, ?, ?, ?, ?)"
            self.mycursor.execute(sql, account_info)
            self.conn.commit()
            return True
        except:
            return False   

    def show_account(self):
        sql = "SELECT * FROM accounts"
        self.mycursor.execute(sql)
        self.results = self.mycursor.fetchall()
        return tuple(self.results)

    def close_connection(self):
        self.conn.close()
