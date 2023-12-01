import tkinter as tk
from tkinter import *
import json
import os

class RegisterationWindow:
    def __init__(self, filename, max_users_allowed, x_offset, y_offset):
        self.filename = filename
        self.max_users_allowed = max_users_allowed
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.register_window = None
        self.register_window_open = False

    def register_screen(self): #Register window pops up
        
       
        def register():

            with open(self.filename, "r") as user_file: user_items = json.load(user_file)  # Open in read mode, load json file and read contents
            num_dicts = sum(isinstance(item, dict) for item in user_items)   # Count the number of dictionaries in the json file

            if ((entry_username.get() == "") or (entry_password.get() == "") or (entry_name.get() == "") or (entry_email.get() == "")):
                label_bottom.config(text="All fields must contain content, please try again")   #If all fields are not filled
            elif (not entry_name.get().replace(" ", "").isalpha()):  #Get rid of spaces as they are allowed for full names
                label_bottom.config(text="Invalid name, only alphabets allowed, please try again")   # If there are non alphabets in the name field
            elif (num_dicts >= self.max_users_allowed):    # If max number of users already in json file
                label_bottom.config(text="The maximum number of user accounts have already been created")
            elif (len(entry_password.get()) <= 7):   #If password is 7 or less characters
                label_bottom.config(text="Password must be at least 8 characters, please try again")
            elif (len(entry_name.get()) >= 35):   #Name shouldn't be too long or displaying it in main screen can cause visual errors
                label_bottom.config(text="Please enter a shorter name and try again")
            elif (any(entry_username.get() == user.get("username") for user in user_items)):  #Making sure same username can't be used again
                label_bottom.config(text="That username is not available, please choose another one")
            else:   #Consolidating inputted user data
                user_items.append({"username": entry_username.get(), "password": entry_password.get(), "name": entry_name.get(), "email": entry_email.get(),
                "SerialNum": num_dicts + 1,
                "parameters": {
                    "AOO_LRL": 126.0,
                    "AOO_URL": 50.0,
                    "AOO_AA": 0.0,
                    "AOO_APW": 0.05,
                    "AAI_LRL": 30.0,
                    "AAI_URL": 50.0,
                    "AAI_AA": 0.0,
                    "AAI_APW": 0.05,
                    "AAI_AS": 0.25,
                    "AAI_ARP": 150.0,
                    "AAI_PVARP": 150.0,
                    "AAI_RS": 0.0,
                    "AAI_H": 0.0,
                    "VOO_LRL": 174.0,
                    "VOO_URL": 51.0,
                    "VOO_VA": 6.9,
                    "VOO_VPW": 1.2,
                    "VVI_LRL": 150.0,
                    "VVI_URL": 175.0,
                    "VVI_VA": 4.0,
                    "VVI_VPW": 0.05,
                    "VVI_VS": 0.25,
                    "VVI_VRP": 300.0,
                    "VVI_H": 0.0,
                    "VVI_RS": 0.0,
                    "AOOR_LRL": 126.0,
                    "AOOR_URL": 50.0,
                    "AOOR_MSR": 55.0,
                    "AOOR_AA": 6.0,
                    "AOOR_APW": 0.05,
                    "AOOR_AT": 5.0,
                    "AOOR_RT": 15.0,
                    "AOOR_RF": 5.0,
                    "AOOR_RTI": 5.0,
                    "AAIR_LRL": 126.0,
                    "AAIR_URL": 50.0,
                    "AAIR_MSR": 55.0,
                    "AAIR_AA": 3.5,
                    "AAIR_APW": 0.05,
                    "AAIR_AS": 5.0,
                    "AAIR_ARP": 0.05,
                    "AAIR_PVARP": 0.05,
                    "AAIR_AT": 3.0,
                    "AAIR_RT": 45.0,
                    "AAIR_RF": 15.0,
                    "AAIR_RTI": 4.0,
                    "VOOR_LRL": 126.0,
                    "VOOR_URL": 126.0,
                    "VOOR_MSR": 126.0,
                    "VOOR_VA": 4.9,
                    "VOOR_VPW": 1.05,
                    "VOOR_AT": 4.0,
                    "VOOR_RT": 23.0,
                    "VOOR_RF": 5.0,
                    "VOOR_RTI": 3.0,
                    "VVIR_LRL": 126.0,
                    "VVIR_URL": 126.0,
                    "VVIR_MSR": 126.0,
                    "VVIR_VA": 6.0,
                    "VVIR_VPW": 1.8,
                    "VVIR_VS": 9.0,
                    "VVIR_VRP": 455.0,
                    "VVIR_AT": 6.0,
                    "VVIR_RT": 45.0,
                    "VVIR_RF": 5.0,
                    "VVIR_RTI": 6.0
                }})
                with open(self.filename, "w") as user_file: 
                    json.dump(user_items, user_file, indent = 4)  #Open in write mode, can't append in json, transfer all contents

                label_bottom.config(text="User has been registered")
                entry_name.delete(0, END)
                entry_email.delete(0, END)      #Make all entry widgets empty
                entry_username.delete(0, END)
                entry_password.delete(0, END)
                if os.path.exists("user_items.json"): os.remove("user_items.json")  #Deleting it incase it remains

        # Create the window, labels, entry widgets, button, etc.
        self.register_window = tk.Tk()
        self.register_window.title("Register")
        self.register_window.geometry(f"400x260+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        self.register_window.protocol("WM_DELETE_WINDOW", self.on_register_window_close)  #Will use the function upon closure
        self.register_window_open = True  #Setting flag to true as window is open now
        self.register_window.resizable(False, False)  #Make window non-resizable 
        label = tk.Label(self.register_window, text="Register a New Account")
        label.pack()
        name_label = tk.Label(self.register_window, text = "Full Name:")
        name_label.pack()
        entry_name = tk.Entry(self.register_window, width=30)
        entry_name.pack()
        email_label = tk.Label(self.register_window, text = "Email:")
        email_label.pack()
        entry_email = tk.Entry(self.register_window, width=30)
        entry_email.pack()
        username_label = tk.Label(self.register_window, text = "Username:")
        username_label.pack()
        entry_username = tk.Entry(self.register_window, width=30)
        entry_username.pack()
        password_label = tk.Label(self.register_window, text="Password:")
        password_label.pack()
        entry_password = tk.Entry(self.register_window, width=30, show="*")  # Use "show" to hide the password
        entry_password.pack()
        button_register = tk.Button(self.register_window, text="Register", command=register)
        button_register.pack(pady=10)
        label_bottom = tk.Label(self.register_window, text="")  #First initialzied as empty, used to display error msgs
        label_bottom.pack()

    def on_register_window_close(self):  #Don't touch, created for closing register_window properly during successful login
        self.register_window.destroy()   #To understand why it's needed, look at the test cases written in documentation
        self.register_window_open = False
        self.register_window = None