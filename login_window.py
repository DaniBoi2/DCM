import tkinter as tk
from tkinter import *
import json
import os

class LoginWindow:
    def __init__(self, filename, welcome, registeration_window, register_window_open, on_register_window_close, x_offset, y_offset, main_screen):
        self.admin_u = "admin" 
        self.admin_p = "dsh"   #admin credentials
        self.backup_file = r"data_files\backup.txt"  #Directory of backup file
        self.filename = filename
        self.welcome = welcome
        self.registeration_window = registeration_window
        self.register_window_open = register_window_open  #Flag from register window
        self.on_register_window_close = on_register_window_close
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.main_screen = main_screen

    def login_screen(self):  #Login window pops up
        with open(self.filename, "r") as file: users = json.load(file)  #Loading contents of json file so they can be read 
        def login():
            if (entry_username.get() == self.admin_u and entry_password.get() == self.admin_p):
                if self.register_window_open: self.registeration_window.withdraw()  #Hidentry_usernamee register screen if its deemed open
                login_window.withdraw()
                self.admin_screen()
            elif (len(users) == 0):  #Displays this message if there are no saved users
                label_bottom.config(text="There are no saved users. Please register")
            else:
                for user in users:
                    if(entry_username.get() == user.get("username") and entry_password.get() == user.get("password")):
                        entry_username.delete(0, END)
                        entry_password.delete(0, END)   #Make entry widgets empty
                        if self.register_window_open: self.registeration_window.withdraw()  #Hide register screen if its deemed open
                        self.welcome.withdraw()  #Hide welcome 
                        login_window.withdraw() #Hide login screen
                        self.main_screen(user.get("name"))  #Go to main screen with user full name so it can be displayed in corner
                    elif(entry_username.get() == "" or entry_password.get() == ""):
                        label_bottom.config(text="Please enter your credentials")
                    elif(entry_username.get() != user.get("username") or entry_password.get() != user.get("password")):
                        label_bottom.config(text="Login Credentials Invalid")
                    else:
                        label_bottom.config(text="Please fill in both username and password fields")

        # Create the window, labels, entry widgets, button, etc.
        login_window = tk.Tk()
        login_window.title("Login")
        login_window.geometry(f"400x210+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        login_window.resizable(False, False)
        top_label = tk.Label(login_window, text="Login into an existing account", )
        top_label.pack()
        username_label = tk.Label(login_window, text = "Username:")
        username_label.pack()
        entry_username = tk.Entry(login_window, width=30)
        entry_username.pack()
        space_label = tk.Label(login_window)
        space_label.pack()
        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        entry_password = tk.Entry(login_window, width=30, show="*")  # Use "show" to hide the password
        entry_password.pack()
        button_login = tk.Button(login_window, text="Login", command=login)
        button_login.pack(pady=10)
        label_bottom = tk.Label(login_window, text="")  #First initialzied as empty, used to display error msgs
        label_bottom.pack()

    def admin_screen(self): #Admin window pops up
        def delete_user_data():  #Reads user data, saves it into txt file, and then opens json file in write mode to delete everything
            with open(self.filename, "r") as user_file: user_items = json.load(user_file)  #Open in read mode and load json file and read contents
            with open(self.backup_file, "a") as backup_txt:  #Save contents to backup txt file, appends to everything else
                for user in user_items: backup_txt.write(json.dumps(user) + "\n")  # Backup every user data by writing it to txt file
            with open(self.filename, "w") as user_file: user_file.write("[]")  #Open in write mode to delete everything, empty json array so it can be appended through registration
            label_bottom.config(text="All data has been deleted!")  
            button_delete.config(state="disabled")      
        
        # Create the window, labels, entry widgets, button, etc.
        admin_page = tk.Tk()
        admin_page.title("Admin Settings")
        admin_page.geometry(f"400x120+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        admin_page.resizable(False, False)
        top_label = tk.Label(admin_page, text="Would you like to delete all saved user data?")
        top_label.pack()
        button_delete = tk.Button(admin_page, text="Delete All User Data", command=delete_user_data)
        button_delete.pack()
        label_bottom = tk.Label(admin_page, text="")
        label_bottom.pack()
        label_bottomName = tk.Label(admin_page, text="Logged in as admin")
        label_bottomName.pack(pady=(20, 0), anchor="n")  # Putting it at bottom 