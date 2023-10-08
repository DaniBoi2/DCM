import tkinter as tk
from tkinter import *
import json
import os

class Pacemaker_GUI():
    def __init__(self): #Constructor and welcome screen
        self.admin_u = "admin" 
        self.admin_p = "dsh"   #admin credentials
        self.max_users_allowed = 10
        self.filename = r"data_files\Users.json"
        self.backup_file = r"data_files\backup.txt"
        self.register_window = None  #Declaring it as instance so its window can be closed from login screen when user enters correct credentials
        self.register_window_open = False  #flag declared due to errors with closing the register window upon successful login

        self.welcome = tk.Tk()
        self.welcome.title("Welcome!")
        self.welcome.geometry("800x300")
        self.welcome.resizable(False, False)

        self.label_top = tk.Label(self.welcome, text="Welcome to the Pacemaker Control Platform!", font=("Helvetica", 22), pady = 30)
        self.label_top.pack()
        self.label_middle = tk.Label(self.welcome, text="Proceed to Login or Registration Below", font=("Helvetica", 17), pady = 15)
        self.label_middle.pack()
        self.button_login = tk.Button(self.welcome, text="Login", font=("Helvetica", 14), command=self.login_screen)
        self.button_login.pack()
        self.button_registration = tk.Button(self.welcome, text="Registration", font=("Helvetica", 14), command=self.register_screen)
        self.button_registration.pack(pady=10)
    
    def run(self):
        self.welcome.mainloop()
    
    def register_screen(self): #Register window pops up
        with open(self.filename, "r") as user_file: user_items = json.load(user_file)  # Open in read mode, load json file and read contents
        num_dicts = sum(isinstance(item, dict) for item in user_items)   # Count the number of dictionaries in the json file
       
        def register():
            if ((entry_username.get() == "") or (entry_password.get() == "") or (entry_name.get() == "") or (entry_email.get() == "")):
                label_bottom.config(text="All fields must contain content, please try again")   #If all fields are not filled
            elif (not entry_name.get().replace(" ", "").isalpha()):  #Get rid of spaces as they are allowed for full names
                label_bottom.config(text="Invalid name, only alphabets allowed, please try again")   # If there are non alphabets in the name field
            elif (num_dicts >=  self.max_users_allowed):    # If max number of users already in json file
                label_bottom.config(text="The maximum number of user accounts have already been created")
            elif (len(entry_password.get()) <= 7):   #If password is 7 or less characters
                label_bottom.config(text="Password must be at least 8 characters, please try again")
            else:   #Consolidating inputted user data
                user_items.append({"username": entry_username.get(), "password": entry_password.get(), "name": entry_name.get(), "email": entry_email.get()})
                
                with open(self.filename, "w") as user_file:  #Open in write mode, can't append in json
                    json.dump(user_items, user_file, indent = 4)  #Transfer all contents to json file

                label_bottom.config(text="User has been registered")
                entry_name.delete(0, END)
                entry_email.delete(0, END)      #Make all entry widgets empty
                entry_username.delete(0, END)
                entry_password.delete(0, END)

                if os.path.exists("user_items.json"): os.remove("user_items.json")  #Deleting it incase it remains

        # Create the window, labels, entry widgets, button, etc.
        self.register_window = tk.Tk()
        self.register_window.title("Register")
        self.register_window.geometry("400x250")
        self.register_window.protocol("WM_DELETE_WINDOW", self.on_register_window_close)  #Will use the function upon closure
        self.register_window_open = True  #Setting flag to true as window is open now
        self.register_window.resizable(False, False)  #Make window non-resizable 
        label = tk.Label(self.register_window, text="Register a New Account")
        label.pack()
        name_label = tk.Label(self.register_window, text = "Full Name:")
        name_label.pack()
        entry_name = tk.Entry(self.register_window)
        entry_name.pack()
        email_label = tk.Label(self.register_window, text = "Email:")
        email_label.pack()
        entry_email = tk.Entry(self.register_window)
        entry_email.pack()
        username_label = tk.Label(self.register_window, text = "Username:")
        username_label.pack()
        entry_username = tk.Entry(self.register_window)
        entry_username.pack()
        password_label = tk.Label(self.register_window, text="Password:")
        password_label.pack()
        entry_password = tk.Entry(self.register_window, show="*")  # Use "show" to hide the password
        entry_password.pack()
        button_register = tk.Button(self.register_window, text="Register", command=register)
        button_register.pack()
        label_bottom = tk.Label(self.register_window, text="")  #First initialzied as empty, used to display error msgs
        label_bottom.pack()
    
    def on_register_window_close(self):  #Don't touch, created for closing register_window properly during successful login
        self.register_window.destroy()
        self.register_window_open = False
        self.register_window = None
    
    def login_screen(self):  #Login window pops up
        with open(self.filename, "r") as file: users = json.load(file)

        def login():
            if (entry_username.get() == self.admin_u and entry_password.get() == self.admin_p):
                label_bottom.config(text="Logging in as administrator")
                entry_username.delete(0, END)   
                entry_password.delete(0, END)   #Make entry widgets empty
                login_window.withdraw()
                self.admin_screen()
            else:
                for user in users:
                    JSON_username = user.get("username")
                    JSON_password = user.get("password")
                    JSON_fullname = user.get("name")
                    
                    if(entry_username.get() == JSON_username and entry_password.get() == JSON_password):
                        entry_username.delete(0, END)
                        entry_password.delete(0, END)   #Make entry widgets empty
                        if self.register_window_open:  #Hide register screen if its deemed open
                            self.register_window.withdraw()
                        self.welcome.withdraw()  #Hide welcome 
                        login_window.withdraw() #Hide login screen
                        self.main_screen(JSON_fullname)  #Go to main screen with user full name so it can be displayed in corner
                    elif(entry_username.get() == "" or entry_password.get() == ""):
                        label_bottom.config(text="Please enter your credentials")
                    elif(entry_username.get() != JSON_username or entry_password.get() != JSON_password):
                        label_bottom.config(text="Login Credentials Invalid")
                    else:
                        label_bottom.config(text="Please fill in both username and password fields")

        # Create the window, labels, entry widgets, button, etc.
        login_window = tk.Tk()
        login_window.title("Login")
        login_window.geometry("400x210")
        login_window.resizable(False, False)
        top_label = tk.Label(login_window, text="Login into an existing account", )
        top_label.pack()
        username_label = tk.Label(login_window, text = "Username:")
        username_label.pack()
        entry_username = tk.Entry(login_window)
        entry_username.pack()
        space_label = tk.Label(login_window)
        space_label.pack()
        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        entry_password = tk.Entry(login_window, show="*")  # Use "show" to hide the password
        entry_password.pack()
        button_login = tk.Button(login_window, text="Login", command=login)
        button_login.pack(pady=10)
        label_bottom = tk.Label(login_window, text="")  #First initialzied as empty, used to display error msgs
        label_bottom.pack()
    
    def admin_screen(self): #Admin window pops up
        def delete_user_data():
            with open(self.filename, "r") as user_file:  #Open in read mode
                user_items = json.load(user_file)  # Load json file and read contents
            with open(self.backup_file, "a") as backup_file:  #Save contents to backup txt file, appends to everything else
                for user in user_items:
                    backup_file.write(json.dumps(user) + "\n")
            with open(self.filename, "w") as user_file:  #Open json file in write mode to delete everything
                user_file.write("[]")  #Write empty json array so it can be appended through registration

            label_bottom.config(text="All data has been deleted!")  
            button_delete.config(state="disabled")      
        
        # Create the window, labels, entry widgets, button, etc.
        admin_page = tk.Tk()
        admin_page.title("Admin Settings")
        admin_page.geometry("400x100")
        admin_page.resizable(False, False)
        top_label = tk.Label(admin_page, text="Would you like to delete all saved user data?")
        top_label.pack()
        button_delete = tk.Button(admin_page, text="Delete All User Data", command=delete_user_data)
        button_delete.pack()
        label_bottom = tk.Label(admin_page, text="")
        label_bottom.pack()

    def main_screen(self,user_name):
        main_window = tk.Tk()
        main_window.title("Pacemaker Control Platform")
        main_window.geometry("800x300")
        main_window.resizable(False, False)
        label_topLeft =tk.Label(main_window, text="Logged in as " + user_name)
        label_topLeft.grid(row=0, column=0, sticky="nw")  # Putting it at top left
    
if __name__ == "__main__":
    pacemaker = Pacemaker_GUI()
    pacemaker.run()