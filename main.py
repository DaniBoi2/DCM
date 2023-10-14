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
    
    def login_screen(self):  #Login window pops up
        with open(self.filename, "r") as file: users = json.load(file)  #Loading contents of json file so they can be read 
        def login():
            if (entry_username.get() == self.admin_u and entry_password.get() == self.admin_p):
                if self.register_window_open: self.register_window.withdraw()  #Hidentry_usernamee register screen if its deemed open
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
        
        with open(self.filename, 'r') as file:
            users = json.load(file)

            user_index = 0
            user = users[user_index]
            print(user)
        def logout(): 
            main_window.withdraw()  #At logout, hide main screen window and show welcome screen again
            self.welcome.deiconify()

        main_window = tk.Tk()
        main_window.title("Pacemaker Control Platform")
        main_window.geometry(f"1200x400+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        main_window.resizable(False, False)
        label_topLeft =tk.Label(main_window, text="Logged in as " + user_name)
        label_topLeft.grid(row=0, column=0, sticky="nw")  # Putting it at top left
        label_top =tk.Label(main_window, text="Pacemaker Control Platform",font=("Helvetica", 15))
        label_top.grid(row=0, column=1, columnspan=2, sticky="n", pady=(0,10))  # Putting it at top
        button_logout = tk.Button(main_window, text="Logout", command=logout)
        button_logout.grid(row=0, column=5, sticky="ne")
        label_state = tk.Label(main_window, text="State")  #Used to show the current state (AOO,VOO...etc)
        label_state.grid(row=2, column=0, sticky="nw")

        

        #Entry widgets for AAO
        entry_LRL_AAO = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AAO.grid(row=3, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AAO.insert(-1, user["parameters"]["AAO_LRL"]) #Default value of 0
        entry_LRL_AAO.grid_remove()

        entry_URL_AAO = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AAO.grid(row=4, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AAO.insert(-1, user["parameters"]["AAO_URL"])  #Default value of 0
        entry_URL_AAO.grid_remove()

        entry_AA_AAO = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AAO.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AAO.insert(-1, user["parameters"]["AAO_AA"])  #Default value of 0
        entry_AA_AAO.grid_remove()

        entry_APW_AAO = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AAO.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AAO.insert(-1, user["parameters"]["AAO_APW"])  #Default value of 0
        entry_APW_AAO.grid_remove()

        #Entry widgets for VOO
        entry_LRL_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VOO.grid(row=3, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VOO.insert(-1, user["parameters"]["VOO_LRL"]) #Default value of 0
        entry_LRL_VOO.grid_remove()

        entry_URL_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VOO.grid(row=4, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VOO.insert(-1, user["parameters"]["VOO_URL"])  #Default value of 0
        entry_URL_VOO.grid_remove()

        entry_VA_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VOO.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VOO.insert(-1, user["parameters"]["VOO_VA"])  #Default value of 0
        entry_VA_VOO.grid_remove()

        entry_VPW_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VOO.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VOO.insert(-1, user["parameters"]["VOO_VPW"])  #Default value of 0
        entry_VPW_VOO.grid_remove()

        #Entry widgets for AAI
        entry_LRL_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AAI.grid(row=3, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AAI.insert(-1, user["parameters"]["AAI_LRL"]) #Default value of 0
        entry_LRL_AAI.grid_remove()
        
        entry_URL_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AAI.grid(row=4, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AAI.insert(-1, user["parameters"]["AAI_URL"])  #Default value of 0
        entry_URL_AAI.grid_remove()
        
        entry_AA_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AAI.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AAI.insert(-1, user["parameters"]["AAI_AA"])  #Default value of 0
        entry_AA_AAI.grid_remove()

        entry_APW_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AAI.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AAI.insert(-1, user["parameters"]["AAI_APW"])  #Default value of 0
        entry_APW_AAI.grid_remove()

        entry_AS_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_AS_AAI.grid(row=3, column=3, pady=(20, 10), padx=(5,0), sticky="w")
        entry_AS_AAI.insert(-1, user["parameters"]["AAI_AS"])  #Default value of 0
        entry_AS_AAI.grid_remove()

        entry_ARP_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_ARP_AAI.grid(row=4, column=3, pady=10, padx=(5,0), sticky="w")
        entry_ARP_AAI.insert(-1, user["parameters"]["AAI_ARP"])  #Default value of 0
        entry_ARP_AAI.grid_remove()

        entry_PVARP_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_PVARP_AAI.grid(row=6, column=3, pady=10, padx=(5,0), sticky="w")
        entry_PVARP_AAI.insert(-1, user["parameters"]["AAI_PVARP"])  #Default value of 0
        entry_PVARP_AAI.grid_remove()

        entry_H_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_H_AAI.grid(row=6, column=3, pady=10, padx=(5,0), sticky="w")
        entry_H_AAI.insert(-1, user["parameters"]["AAI_H"])  #Default value of 0
        entry_H_AAI.grid_remove()

        entry_RS_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_RS_AAI.grid(row=6, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RS_AAI.insert(-1, user["parameters"]["AAI_RS"])  #Default value of 0
        entry_RS_AAI.grid_remove()

        #Entry widgets for VVI
        entry_LRL_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VVI.grid(row=3, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VVI.insert(-1, user["parameters"]["VVI_LRL"]) #Default value of 0
        entry_LRL_VVI.grid_remove()

        entry_URL_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VVI.grid(row=4, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VVI.insert(-1, user["parameters"]["VVI_URL"])  #Default value of 0
        entry_URL_VVI.grid_remove()

        entry_VA_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VVI.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VVI.insert(-1, user["parameters"]["VVI_VA"])  #Default value of 0
        entry_VA_VVI.grid_remove()

        entry_VPW_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VVI.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VVI.insert(-1, user["parameters"]["VVI_VPW"])  #Default value of 0
        entry_VPW_VVI.grid_remove()

        entry_VS_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VS_VVI.grid(row=9, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VS_VVI.insert(-1, user["parameters"]["VVI_VS"])  #Default value of 0
        entry_VS_VVI.grid_remove()

        entry_VRP_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VRP_VVI.grid(row=5, column=3, pady=10, padx=(5,0), sticky="w")
        entry_VRP_VVI.insert(-1, user["parameters"]["VVI_VRP"])  #Default value of 0
        entry_VRP_VVI.grid_remove()

        entry_H_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_H_VVI.grid(row=7, column=3, pady=10, padx=(5,0), sticky="w")
        entry_H_VVI.insert(-1, user["parameters"]["VVI_H"])  #Default value of 0
        entry_H_VVI.grid_remove()

        entry_RS_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_RS_VVI.grid(row=8, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RS_VVI.insert(-1, user["parameters"]["VVI_RS"])  #Default value of 0
        entry_RS_VVI.grid_remove()
    
        
        self.welcome.deiconify()
        def AOO_pressed():
            label_state.config(text="State:  AOO")

            # grid_remove hides the widgets of states, but keeps their values
            entry_LRL_VOO.grid_remove()
            entry_URL_VOO.grid_remove()
            entry_VA_VOO.grid_remove()
            entry_VPW_VOO.grid_remove()
            
            entry_LRL_AAI.grid_remove()
            entry_URL_AAI.grid_remove()
            entry_AA_AAI.grid_remove()
            entry_APW_AAI.grid_remove()
            entry_AS_AAI.grid_remove()
            entry_ARP_AAI.grid_remove()
            entry_PVARP_AAI.grid_remove()
            entry_H_AAI.grid_remove()
            entry_RS_AAI.grid_remove()

            entry_LRL_VVI.grid_remove()
            entry_URL_VVI.grid_remove()
            entry_VA_VVI.grid_remove()
            entry_VPW_VVI.grid_remove()
            entry_VS_VVI.grid_remove()
            entry_VRP_VVI.grid_remove()
            entry_H_VVI.grid_remove()
            entry_RS_VVI.grid_remove()


            entry_LRL_AAO.grid()
            entry_URL_AAO.grid()
            entry_AA_AAO.grid()
            entry_APW_AAO.grid()

            

        def VOO_pressed():
            label_state.config(text="State:  VOO")

            entry_LRL_AAI.grid_remove()
            entry_URL_AAI.grid_remove()
            entry_AA_AAI.grid_remove()
            entry_APW_AAI.grid_remove()
            entry_AS_AAI.grid_remove()
            entry_ARP_AAI.grid_remove()
            entry_PVARP_AAI.grid_remove()
            entry_H_AAI.grid_remove()
            entry_RS_AAI.grid_remove()

            entry_LRL_AAO.grid_remove()
            entry_URL_AAO.grid_remove()
            entry_AA_AAO.grid_remove()
            entry_APW_AAO.grid_remove()

            entry_LRL_VVI.grid_remove()
            entry_URL_VVI.grid_remove()
            entry_VA_VVI.grid_remove()
            entry_VPW_VVI.grid_remove()
            entry_VS_VVI.grid_remove()
            entry_VRP_VVI.grid_remove()
            entry_H_VVI.grid_remove()
            entry_RS_VVI.grid_remove()


            entry_LRL_VOO.grid()
            entry_URL_VOO.grid()
            entry_VA_VOO.grid()
            entry_VPW_VOO.grid()



        def AAI_pressed():
            label_state.config(text="State:  AAI")

            entry_LRL_AAO.grid_remove()
            entry_URL_AAO.grid_remove()
            entry_AA_AAO.grid_remove()
            entry_APW_AAO.grid_remove()

            entry_LRL_VOO.grid_remove()
            entry_URL_VOO.grid_remove()
            entry_VA_VOO.grid_remove()
            entry_VPW_VOO.grid_remove()

            entry_LRL_VVI.grid_remove()
            entry_URL_VVI.grid_remove()
            entry_VA_VVI.grid_remove()
            entry_VPW_VVI.grid_remove()
            entry_VS_VVI.grid_remove()
            entry_VRP_VVI.grid_remove()
            entry_H_VVI.grid_remove()
            entry_RS_VVI.grid_remove()


            entry_LRL_AAI.grid()
            entry_URL_AAI.grid()
            entry_AA_AAI.grid()
            entry_APW_AAI.grid()
            entry_AS_AAI.grid()
            entry_ARP_AAI.grid()
            entry_PVARP_AAI.grid()
            entry_H_AAI.grid()
            entry_RS_AAI.grid()

            

        def VVI_pressed():
            label_state.config(text="State:  VVI")

            entry_LRL_AAO.grid_remove()
            entry_URL_AAO.grid_remove()
            entry_AA_AAO.grid_remove()
            entry_APW_AAO.grid_remove()

            entry_LRL_VOO.grid_remove()
            entry_URL_VOO.grid_remove()
            entry_VA_VOO.grid_remove()
            entry_VPW_VOO.grid_remove()

            entry_LRL_AAI.grid_remove()
            entry_URL_AAI.grid_remove()
            entry_AA_AAI.grid_remove()
            entry_APW_AAI.grid_remove()
            entry_AS_AAI.grid_remove()
            entry_ARP_AAI.grid_remove()
            entry_PVARP_AAI.grid_remove()
            entry_H_AAI.grid_remove()
            entry_RS_AAI.grid_remove()

            entry_LRL_VVI.grid()
            entry_URL_VVI.grid()
            entry_VA_VVI.grid()
            entry_VPW_VVI.grid()
            entry_VS_VVI.grid()
            entry_VRP_VVI.grid()
            entry_H_VVI.grid()
            entry_RS_VVI.grid()

        def save_state(user_name):
             # Load the existing user data from the JSON file.
            with open(self.filename, 'r') as file:
             users = json.load(file)

    # Find the user with the matching username.
            for user in users:
                if user['name'] == user_name:
                    # Update the 'parameters' field with the parameter values from the app.
                    user['parameters'] = {
                        # AOO
                        "AAO_LRL": float(entry_LRL_AAO.get()),
                        "AAO_URL": float(entry_URL_AAO.get()),
                        "AAO_AA": float(entry_AA_AAO.get()),
                        "AAO_APW": float(entry_APW_AAO.get()),

                        "AAI_LRL": float(entry_LRL_AAI.get()),
                        "AAI_URL": float(entry_URL_AAI.get()),
                        "AAI_AA": float(entry_AA_AAI.get()),
                        "AAI_APW": float(entry_APW_AAI.get()),
                        "AAI_AS": float(entry_AS_AAI.get()),
                        "AAI_ARP": float(entry_ARP_AAI.get()),
                        "AAI_PVARP": float(entry_PVARP_AAI.get()),
                        "AAI_RS": float(entry_RS_AAI.get()),
                        "AAI_H": float(entry_H_AAI.get()),

                        # VOO
                        "VOO_LRL": float(entry_LRL_VOO.get()),
                        "VOO_URL": float(entry_URL_VOO.get()),
                        "VOO_VA": float(entry_VA_VOO.get()),
                        "VOO_VPW": float(entry_VPW_VOO.get()),

                        # VVI
                        "VVI_LRL": float(entry_LRL_VVI.get()),
                        "VVI_URL": float(entry_URL_VVI.get()),
                        "VVI_VA": float(entry_VA_VVI.get()),
                        "VVI_VPW": float(entry_VPW_VVI.get()),
                        "VVI_VS": float(entry_VS_VVI.get()),
                        "VVI_VRP": float(entry_VRP_VVI.get()),
                        "VVI_H": float(entry_H_VVI.get()),
                        "VVI_RS": float(entry_RS_VVI.get())
                    }


                    break  # Stop searching once the user is found.
            
            # Save the updated user data back to the JSON file.
            with open(self.filename, 'w') as file:
                json.dump(users, file, indent=4)

        

        # 4 Buttons for AOO,VOO,AAI,VVI
        button_AOO = tk.Button(main_window, text="AOO", command=AOO_pressed)
        button_AOO.grid(row=2, column=0, sticky="n", padx=(130,65))  #Extra padding on its left side so its equal distance away from the edge
        button_VOO = tk.Button(main_window, text="VOO", command=VOO_pressed)
        button_VOO.grid(row=2, column=2, sticky="n", padx=65)
        button_AAI = tk.Button(main_window, text="AAI", command=AAI_pressed)
        button_AAI.grid(row=2, column=1, sticky="n", padx=65)
        button_VVI = tk.Button(main_window, text="VVI", command=VVI_pressed)
        button_VVI.grid(row=2, column=3, sticky="n", padx=65)

        button_save_state = tk.Button(main_window, text = "Save State", command=lambda : save_state(user_name))
        button_save_state.grid(row = 5, column = 5)

        #Displaying programmable parameters labels in left column
        label_lower_rate_limit = tk.Label(main_window, text="Lower Rate Limit (ppm) (30-175)")
        label_lower_rate_limit.grid(row=3, column=0, pady=(20,10), padx=(20,0), sticky="w")
        label_upper_rate_limit = tk.Label(main_window, text="Upper Rate Limit (ppm) (50-175)")
        label_upper_rate_limit.grid(row=4, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_amp = tk.Label(main_window, text="Atrial Amplitude (Volts) (0,0.5-3.2,3.5-7.0)")
        label_atrial_amp.grid(row=5, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_pulse_width = tk.Label(main_window, text="Atrial Pulse Width (nanoseconds) (0.05, 0.1 - 1.9)")
        label_atrial_pulse_width.grid(row=6, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_amp = tk.Label(main_window, text="Ventricular Amplitude (Volts) (0,0.5-3.2,3.5-7.0)")
        label_ventricular_amp.grid(row=7, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_pulse_width = tk.Label(main_window, text="Ventricular Pulse Width (Nanoseconds) (0.05, 0.1 - 1.9)")
        label_ventricular_pulse_width.grid(row=8, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_sensitivity = tk.Label(main_window, text="Ventricular Sensitivity (milivolts) (0.25, 0.5, 0.75, 1.0 - 10)")
        label_ventricular_sensitivity.grid(row=9, column=0, pady=10, padx=(20,0), sticky="w")

       

        #Displaying programmable parameters labels in 2nd column
        label_atrial_sensitivity = tk.Label(main_window, text="Atrial Sensitivity (milivolts) (0.25, 0.5, 0.75, 1.0 - 10)")
        label_atrial_sensitivity.grid(row=3, column=2, pady=(20,10), padx=(20,0), sticky="w")
        label_ARP = tk.Label(main_window, text="ARP (miliseconds) (150 - 500)")
        label_ARP.grid(row=4, column=2, pady=10, padx=(20,0), sticky="w")
        label_VRP = tk.Label(main_window, text="VRP (miliseconds) (150 - 500)")
        label_VRP.grid(row=5, column=2, pady=10, padx=(20,0), sticky="w")
        label_PVARP = tk.Label(main_window, text="PVARP (miliseconds) (150 - 500)")
        label_PVARP.grid(row=6, column=2, pady=10, padx=(20,0), sticky="w")
        label_hysteresis = tk.Label(main_window, text="Hysteresis (ppm) (Off or 30-175)")
        label_hysteresis.grid(row=7, column=2, pady=10, padx=(20,0), sticky="w")
        label_rate_smoothing = tk.Label(main_window, text="Rate Smoothing (%) (Off, 3, 6, 9, 12, 15, 18, 21, 25)")
        label_rate_smoothing.grid(row=8, column=2, pady=10, padx=(20,0), sticky="w")
    
if __name__ == "__main__": #Used to make sure that the program is run directly and that it's not imported anywhere
    pacemaker = Pacemaker_GUI()
    pacemaker.run()