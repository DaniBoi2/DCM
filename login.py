import tkinter as tk
from tkinter import *
import json
import time
from register import register_file
#from main_screen import main_screen_file
from adminWindow import admin_file
admin_u = "admin"
admin_p = "dsh"
filename = r"data_files\Users.json"

def login_file():
    with open(filename, "r") as file:
        users = json.load(file)

    def login():
        username_text = entry_username.get()
        password_text = entry_password.get()

        if (username_text == admin_u and password_text == admin_p):
            label_bottom.config(text="Logging in as administrator")
            entry_username.delete(0, END)   
            entry_password.delete(0, END)   #Make entry widgets empty
            goto_adminWindow()
        else:
            for user in users:
                JSON_username = user.get("username")
                JSON_password = user.get("password")
                JSON_fullname = user.get("name")
                
                if(username_text == JSON_username and password_text == JSON_password):
                    entry_username.delete(0, END)
                    entry_password.delete(0, END)   #Make entry widgets empty
                    label_bottom.config(text="Logging in as " + JSON_fullname)
                    goto_mainScreen()
                elif(username_text != JSON_username or password_text != JSON_password):
                    label_bottom.config(text="Login Credential INVALID")
                else:
                    label_bottom.config(text="Please fill in both username and password fields")

    def goto_registration():  #Used to open registration window if user hits register button
        entry_username.delete(0, END)   
        entry_password.delete(0, END)   #Make entry widgets empty
        label_bottom.config(text="")   #Make bottom label text empty
        register_file()   #Go to register file
    
    def goto_mainScreen():  #Used to go to main screen of the program with all of the stateflow settings
        login_window.withdraw()
        #main_screen_file()

    def goto_adminWindow():  #Goes to admin window where users.json contents can be deleted
        login_window.withdraw()
        admin_file()

    # Create the main window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x210")
    login_window.resizable(False, False)

    # Create a top label
    top_label = tk.Label(login_window, text="Login into an existing account", )
    top_label.pack()

    # Create an entry widget and label for username
    username_label = tk.Label(login_window, text = "Username:")
    username_label.pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    # Create an entry widget and label for password
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    entry_password = tk.Entry(login_window, show="*")  # Use "show" to hide the password
    entry_password.pack()

    # Create a login button
    button_login = tk.Button(login_window, text="Login", command=login)
    button_login.pack()

    #Create a bottom label
    label_bottom = tk.Label(login_window, text="")
    label_bottom.pack()

    # Create a button to open register functionality
    registration_button = tk.Button(login_window, text="Don't have an account? Register", command=goto_registration)
    registration_button.pack(side="left", padx = 10, pady = 20)

    # Run the Tkinter main loop
    login_window.mainloop()
