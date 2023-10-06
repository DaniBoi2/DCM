import tkinter as tk
import json
import os
max_users_allowed = 10

user_data_file = "Users.json"
with open(user_data_file, "r") as user_file:  #Open in read mode
    user_items = json.load(user_file)
num_dicts = sum(isinstance(item, dict) for item in user_items)   # Count the number of dictionaries in the json file
user_file.close()
    
def register():
    if num_dicts >= max_users_allowed:
        label.config(text="The maximum number of user accounts have already been created")
    else:
        username_text = entry_username.get()
        password_text = entry_password.get()
        name_text = entry_name.get()
        email_text = entry_email.get()
        user_items.append({"username": username_text, "password": password_text, "name": name_text, "email": email_text})
        
        with open(user_data_file, "w") as user_file:  #Open in write mode, can't append in json
            json.dump(user_items, user_file, indent = 4)
        user_file.close()
        label.config(text="User has been registered")

        if os.path.exists("user_items.json"): # Deleting it after its contents have been added to our main file
            os.remove("user_items.json")

# Create the main window
register_window = tk.Tk()
register_window.title("Register")
register_window.geometry("400x280")

# Create a label
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

# Run the Tkinter main loop
register_window.mainloop()
