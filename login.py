import tkinter as tk
import json

filename = "Users.json"

with open(filename, "r") as file:
    users = json.load(file)

def login():
    username_text = entry_username.get()
    password_text = entry_password.get()
    
    
    for user in users:
        JSON_username = user.get("username")
        JSON_password = user.get("password")
        JSON_fullname = user.get("name")
        if(username_text == JSON_username and password_text == JSON_password):
            label.config(text="Logging in as " + JSON_fullname)
            return

        elif(username_text != JSON_username or password_text != JSON_password):
            label.config(text="Login Credential INVALID")

        else:
            label.config(text="Please fill in both username and password fields")

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("400x200")

# Create a label
label = tk.Label(root, text="Login into an existing account", )
label.pack()

username_label = tk.Label(root, text = "Username:")
username_label.pack()

# Create an entry widget for username
entry_username = tk.Entry(root)
entry_username.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

# Create an entry widget for password
entry_password = tk.Entry(root, show="*")  # Use "show" to hide the password
entry_password.pack()

# Create a login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

# Run the Tkinter main loop
root.mainloop()
