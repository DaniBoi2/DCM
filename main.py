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
        self.width_screen = self.welcome.winfo_screenwidth() # width of the user screen
        self.height_screen = self.welcome.winfo_screenheight() # height of the user screen
        self.x_offset = int((self.width_screen/2) - (800/2) - 40) # calculate x offset coordinates for the window position
        self.y_offset = int((self.height_screen/2) - (300/2) - 80)  # calculate y offset coordinates for the window position
        self.welcome.title("Welcome!")
        self.welcome.geometry(f"800x300+{self.x_offset}+{self.y_offset}") #Displaying it in the center of the user screen
        self.welcome.resizable(False, False)
        self.label_top = tk.Label(self.welcome, text="Welcome to the Pacemaker Control Platform!", font=("Helvetica", 22), pady = 30)
        self.label_top.pack()
        self.label_middle = tk.Label(self.welcome, text="Proceed to Login or Registration Below", font=("Helvetica", 17), pady = 15)
        self.label_middle.pack()
        self.button_login = tk.Button(self.welcome, text="Login", font=("Helvetica", 14), command=self.login_screen)
        self.button_login.pack()
        self.button_registration = tk.Button(self.welcome, text="Registration", font=("Helvetica", 14), command=self.register_screen)
        self.button_registration.pack(pady=10)
        self.button_exit = tk.Button(self.welcome, text="Exit", font=("Helvetica", 12), command=exit)  #Used to properly close the program
        self.button_exit.pack(side="left", padx=10)

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
            elif (num_dicts >= self.max_users_allowed):    # If max number of users already in json file
                label_bottom.config(text="The maximum number of user accounts have already been created")
            elif (len(entry_password.get()) <= 7):   #If password is 7 or less characters
                label_bottom.config(text="Password must be at least 8 characters, please try again")
            elif (len(entry_name.get()) >= 35):   #Name shouldn't be too long or displaying it in main screen can cause visual errors
                label_bottom.config(text="Please enter a shorter name and try again")
            elif (any(entry_username.get() == user.get("username") for user in user_items)):  #Making sure same username can't be used again
                label_bottom.config(text="That username is not available, please choose another one")
            else:   #Consolidating inputted user data
                user_items.append({"username": entry_username.get(), "password": entry_password.get(), "name": entry_name.get(), "email": entry_email.get()})
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
        self.register_window.geometry(f"400x250+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
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
        self.register_window.destroy()   #To understand why it's needed, look at the test cases written in documentation
        self.register_window_open = False
        self.register_window = None
    
    def login_screen(self):  #Login window pops up
        with open(self.filename, "r") as file: users = json.load(file)  #Loading contents of json file so they can be read 
        def login():
            if (entry_username.get() == self.admin_u and entry_password.get() == self.admin_p):
                if self.register_window_open: self.register_window.withdraw()  #Hide register screen if its deemed open
                login_window.withdraw()
                self.admin_screen()
            elif (len(users) == 0):  #Displays this message if there are no saved users
                label_bottom.config(text="There are no saved users. Please register")
            else:
                for user in users:
                    if(entry_username.get() == user.get("username") and entry_password.get() == user.get("password")):
                        entry_username.delete(0, END)
                        entry_password.delete(0, END)   #Make entry widgets empty
                        if self.register_window_open: self.register_window.withdraw()  #Hide register screen if its deemed open
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
        def delete_user_data():  #Reads user data, saves it into txt file, and then opens json file in write mode to delete everything
            with open(self.filename, "r") as user_file: user_items = json.load(user_file)  #Open in read mode and load json file and read contents
            with open(self.backup_file, "a") as backup_file:  #Save contents to backup txt file, appends to everything else
                for user in user_items: backup_file.write(json.dumps(user) + "\n")  # Backup every user data by writing it to txt file
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

    def main_screen(self,user_name): #Main screen pops up, user_name as input so it can display "Logged in as [user_name]" 
        def logout(): 
            main_window.withdraw()  #At logout, hide main screen window and show welcome screen again
            self.welcome.deiconify()
        def AOO_pressed():
            label_state.config(text="State:  AOO")
        def VOO_pressed():
            label_state.config(text="State:  VOO")
        def AAI_pressed():
            label_state.config(text="State:  AAI")
        def VVI_pressed():
            label_state.config(text="State:  VVI")

        main_window = tk.Tk()
        main_window.title("Pacemaker Control Platform")
        main_window.geometry(f"810x400+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        main_window.resizable(False, False)
        label_topLeft =tk.Label(main_window, text="Logged in as " + user_name)
        label_topLeft.grid(row=0, column=0, sticky="nw")  # Putting it at top left
        label_top =tk.Label(main_window, text="Pacemaker Control Platform",font=("Helvetica", 15))
        label_top.grid(row=0, column=1, columnspan=2, sticky="n", pady=(0,10))  # Putting it at top
        button_logout = tk.Button(main_window, text="Logout", command=logout)
        button_logout.grid(row=0, column=5, sticky="ne")
        label_state = tk.Label(main_window, text="State")  #Used to show the current state (AOO,VOO...etc)
        label_state.grid(row=2, column=0, sticky="nw")

        # 4 Buttons for AOO,VOO,AAI,VVI
        button_AOO = tk.Button(main_window, text="AOO", command=AOO_pressed)
        button_AOO.grid(row=2, column=0, sticky="n", padx=(130,65))  #Extra padding on its left side so its equal distance away from the edge
        button_VOO = tk.Button(main_window, text="VOO", command=VOO_pressed)
        button_VOO.grid(row=2, column=2, sticky="n", padx=65)
        button_AAI = tk.Button(main_window, text="AAI", command=AAI_pressed)
        button_AAI.grid(row=2, column=1, sticky="n", padx=65)
        button_VVI = tk.Button(main_window, text="VVI", command=VVI_pressed)
        button_VVI.grid(row=2, column=3, sticky="n", padx=65)

        #Displaying programmable parameters labels in left column
        label_lower_rate_limit = tk.Label(main_window, text="Lower Rate Limit (units) (range)")
        label_lower_rate_limit.grid(row=3, column=0, pady=(20,10), padx=(20,0), sticky="w")
        label_upper_rate_limit = tk.Label(main_window, text="Upper Rate Limit (units) (range)")
        label_upper_rate_limit.grid(row=4, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_amp = tk.Label(main_window, text="Atrial Amplitude (units) (range)")
        label_atrial_amp.grid(row=5, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_pulse_width = tk.Label(main_window, text="Atrial Pulse Width (units) (range)")
        label_atrial_pulse_width.grid(row=6, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_amp = tk.Label(main_window, text="Ventricular Amplitude (units) (range)")
        label_ventricular_amp.grid(row=7, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_pulse_width = tk.Label(main_window, text="Ventricular Pulse Width (units) (range)")
        label_ventricular_pulse_width.grid(row=8, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_sensitivity = tk.Label(main_window, text="Ventricular Sensitivity (units) (range)")
        label_ventricular_sensitivity.grid(row=9, column=0, pady=10, padx=(20,0), sticky="w")

        #Displaying programmable parameters labels in 2nd column
        label_atrial_sensitivity = tk.Label(main_window, text="Atrial Sensitivity (units) (range)")
        label_atrial_sensitivity.grid(row=3, column=2, pady=(20,10), padx=(20,0), sticky="w")
        label_ARP = tk.Label(main_window, text="ARP (units) (range)")
        label_ARP.grid(row=4, column=2, pady=10, padx=(20,0), sticky="w")
        label_VRP = tk.Label(main_window, text="VRP (units) (range)")
        label_VRP.grid(row=5, column=2, pady=10, padx=(20,0), sticky="w")
        label_PVARP = tk.Label(main_window, text="PVARP (units) (range)")
        label_PVARP.grid(row=6, column=2, pady=10, padx=(20,0), sticky="w")
        label_hysteresis = tk.Label(main_window, text="Hysteresis (units) (range)")
        label_hysteresis.grid(row=7, column=2, pady=10, padx=(20,0), sticky="w")
        label_rate_smoothing = tk.Label(main_window, text="Rate Smoothing (units) (range)")
        label_rate_smoothing.grid(row=8, column=2, pady=10, padx=(20,0), sticky="w")
    
if __name__ == "__main__": #Used to make sure that the program is run directly and that it's not imported anywhere
    pacemaker = Pacemaker_GUI()
    pacemaker.run()