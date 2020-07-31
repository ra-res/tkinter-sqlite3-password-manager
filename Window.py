from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
import termtables as tt
import mysql.connector
from mysql.connector import errorcode
import random
import string
import SQLCon as sql
import Password as p

from secrets import connection_data


class Window():
    def __init__(self, master):
        self.master = master
        self.colour_bg = "Grey"  
        self.colour_err = "Red"      
        self.draw_widgets()
        self.random_password_size = 15
        self.dbcon = sql.SQLCon()
        self.password = p.Password()

    def add_new_password_screen(self):
        self.c.destroy()
        self.draw_canvas()

        self.c.web_label = Label(self.c, text="Website Name:", bg=self.colour_bg , font =("",15)).grid(row=0, column=0)
        self.c.web_entry = Entry(self.c, text="website_name", font=("",15))
        self.c.web_entry.grid(row=0, column=1)

        self.c.username_label = Label(self.c, text="Username:", bg=self.colour_bg ,font =("",15)).grid(row=1, column=0)
        self.c.username_entry = Entry(self.c, text="username", font=("",15))
        self.c.username_entry.grid(row=1, column=1)

        self.c.password_label = Label(self.c, text="Password:",bg=self.colour_bg , font =("",15)).grid(row=2, column=0)
        self.c.password_entry = Entry(self.c, text="password", show="*", font=("",15))
        self.c.password_entry.grid(row=2, column=1)

        self.c.password2_label = Label(self.c, text="Password2:",bg=self.colour_bg , font =("",15)).grid(row=3, column=0)
        self.c.password2_entry = Entry(self.c, text="password2", show="*", font=("",15))
        self.c.password2_entry.grid(row=3, column=1)

        self.c.add_password_button = tk.Button(self.c, text="Save Password", command=self.data_filter ,font =("",15)).grid(row=4, column=1)
        self.c.wants_random_password = tk.Button(self.c, text="Random Pass", command=self.generate_random_password,font =("",15)).grid(row=2, column=2)

        self.c.pack()

    def data_filter(self):
        account_information = {"website_name": self.c.web_entry.get(), 
                "username": self.c.username_entry.get(),
                "password": self.c.password_entry.get(),
                "password_verify": self.c.password2_entry.get() 
                }

        # self.generate_random_password(self.random_password_size)    
        
        for key in account_information:
            if account_information[key] == "" or account_information[key] == None:
                Label(self.c, text="Please fill in the {} box".format(key), bg=self.colour_err, font =("",15)).grid(row=7, column=1)
                return 
        if account_information["password"] != account_information["password_verify"]:
            Label(self.c, text="Passwords Must Match!", bg=self.colour_err, font =("",15)).grid(row=6, column=1)
            return

        _hash, _key = self.password.password_encrypt(account_information['password'])
        commit_data = (account_information['website_name'], account_information['username'], _hash, _key)
        result = self.dbcon.write_account(commit_data)
        if result:
            Label(self.c, text="Successfully entered account", bg=self.colour_err, font =("",15)).grid(row=7, column=1)
        else:
            Label(self.c, text="Error!", bg=self.colour_err, font =("",15)).grid(row=7, column=1)
    


    def generate_random_password(self):
        configuration = string.ascii_letters
        randomised_password = ''.join(random.choice(configuration) for i in range(self.random_password_size))
        self.c.password_entry.delete(0,END)
        self.c.password_entry.insert(0,randomised_password)
        self.c.password2_entry.delete(0,END)
        self.c.password2_entry.insert(0,randomised_password)

    def view_passwords_screen(self):
        self.c.destroy()
        self.draw_canvas()
        Label(self.c, text="Website    ", bg=self.colour_bg , font =("",15)).grid(row=0, column=0)
        Label(self.c, text="Username    ", bg=self.colour_bg , font =("",15)).grid(row=0, column=1)
        Label(self.c, text="Password    ", bg=self.colour_bg , font =("",15)).grid(row=0, column=2)
        # Label(self.c, text=str("_"*25), bg=self.colour_bg , font =("",15)).grid(row=1, column=0)

        accounts = self.dbcon.show_account()
        # print(len(self.accounts))
        for i in range(len(accounts)):
            Label(self.c, text=accounts[i][1], bg=self.colour_bg , font =("",15)).grid(row=i+1, column=0)
            Label(self.c, text=accounts[i][2], bg=self.colour_bg , font =("",15)).grid(row=i+1, column=1)
            Label(self.c, text=self.password.password_decrypt(accounts[i][3], accounts[i][4]), bg=self.colour_bg , font =("",15)).grid(row=i+1, column=2)
        self.c.pack()

    def draw_widgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Button(self.controls, text="New Password", command=self.add_new_password_screen ,font =("",15)).grid(row=0, column=0)
        Button(self.controls, text="View Passwords", command=self.view_passwords_screen ,font =("",15)).grid(row=0, column=1)
        # Button(self.controls, text="View Passwords", command=self.add ,font =("",15)).grid(row=0, column=2)
        self.controls.pack()
        self.draw_canvas()

    def draw_canvas(self):
        self.c = Canvas(self.master, bg=self.colour_bg)
        self.c.pack(fill=BOTH, expand=True)    
    

if __name__=='__main__':
    root = Tk()
    Window(root)
    root.title("Password Manager")  
    root.geometry("500x1000")
    root.resizable(width=False, height=False)
    root.mainloop()              