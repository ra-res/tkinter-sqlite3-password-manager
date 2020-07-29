import mysql.connector
from mysql.connector import errorcode
from secrets import connection_data
# mycursor.execute("SELECT * FROM accounts")
# myresult = mycursor.fetchall()

class SQLCon():
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(user=connection_data["user"],
                            database=connection_data["db"])
            self.mycursor = self.conn.cursor() 
        except Exception as e:
                print(e)                

    def write_account(self):
        pass

    def show_account(self):
        sql = "SELECT * FROM accounts"
        self.mycursor.execute(sql)
        self.results = self.mycursor.fetchall()
        # print(self.results)
        return tuple(self.results)

    def close_connection(self):
        self.conn.close()

c = SQLCon()
c.show_account()