import tkinter as tk
from tkinter import *
import json
import os
max_users_allowed = 10

def register_file():
    user_data_file = r"data_files\Users.json"
    with open(user_data_file, "r") as user_file:  #Open in read mode
        user_items = json.load(user_file)  # Load json file and read contents
    num_dicts = sum(isinstance(item, dict) for item in user_items)   # Count the number of dictionaries in the json file
        
    def register():
        if ((entry_username.get() == "") or (entry_password.get() == "") or (entry_name.get() == "") or (entry_email.get() == "")):
            label_bottom.config(text="All fields must contain content, please try again")   #If all fields are not filled
        elif (not entry_name.get().replace(" ", "").isalpha()):  #Spaces are allowed for full names, so it gets rid of them first
            label_bottom.config(text="Invalid name, only alphabets allowed, please try again")   # If there are non alphabets in the name field
        elif (num_dicts >= max_users_allowed):    # If max number of users already in json file
            label_bottom.config(text="The maximum number of user accounts have already been created")
        elif (len(entry_password.get()) <= 7):   #If password is 7 or less characters
            label_bottom.config(text="Password must be at least 8 characters, please try again")
        else:   #Consolidating inputted user data
            user_items.append({"username": entry_username.get(), "password": entry_password.get(), "name": entry_name.get(), "email": entry_email.get()})
            
            with open(user_data_file, "w") as user_file:  #Open in write mode, can't append in json
                json.dump(user_items, user_file, indent = 4)  #Transfer all contents to json file

            label_bottom.config(text="User has been registered")
            entry_name.delete(0, END)
            entry_email.delete(0, END)      #Make all entry widgets empty
            entry_username.delete(0, END)
            entry_password.delete(0, END)

            if os.path.exists("user_items.json"): # Deleting it after its contents have been added to our main file
                os.remove("user_items.json")

    # Create the main window
    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("400x250")
    register_window.resizable(False, False)  #Make window non-resizable 

    # Create a top label
    label = tk.Label(register_window, text="Register a New Account")
    label.pack()

    # Create a label for name and an entry widget for name
    name_label = tk.Label(register_window, text = "Full Name:")
    name_label.pack()
    entry_name = tk.Entry(register_window)
    entry_name.pack()

    # Create a label for email and an entry widget for email
    email_label = tk.Label(register_window, text = "Email:")
    email_label.pack()
    entry_email = tk.Entry(register_window)
    entry_email.pack()

    # Create a label for username and an entry widget for username
    username_label = tk.Label(register_window, text = "Username:")
    username_label.pack()
    entry_username = tk.Entry(register_window)
    entry_username.pack()

    # Create a label for password and an entry widget for password
    password_label = tk.Label(register_window, text="Password:")
    password_label.pack()
    entry_password = tk.Entry(register_window, show="*")  # Use "show" to hide the password
    entry_password.pack()

    # Create a login button
    button_register = tk.Button(register_window, text="Register", command=register)
    button_register.pack()

    #Create a bottom label for displaying messages
    label_bottom = tk.Label(register_window, text="")
    label_bottom.pack()

    # Run the Tkinter main loop
    register_window.mainloop()