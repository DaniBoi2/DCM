import tkinter as tk
from registeration_window import RegisterationWindow
from main_screen import MainScreen
from login_window import LoginWindow

class Pacemaker_GUI():
    def __init__(self): #Constructor 
        self.max_users_allowed = 10
        self.filename = r"data_files\Users.json"  #Directory of the json file containing all user data
        
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

        # init other classes 
        self.registeration_window = RegisterationWindow(self.filename, self.max_users_allowed, self.x_offset, self.y_offset)
        self.main_screen = MainScreen(self.filename, self.x_offset, self.y_offset, self.welcome)
        self.login_window = LoginWindow(self.filename, self.welcome, self.registeration_window, 
        self.registeration_window.register_window_open, self.registeration_window.on_register_window_close, self.x_offset, self.y_offset,
        self.main_screen.main_screen)

        self.button_login = tk.Button(self.welcome, text="Login", font=("Helvetica", 14), command=self.login_window.login_screen)
        self.button_login.pack()
        self.button_registration = tk.Button(self.welcome, text="Registration", font=("Helvetica", 14), command=self.registeration_window.register_screen)
        self.button_registration.pack(pady=10)
        self.button_exit = tk.Button(self.welcome, text="Exit", font=("Helvetica", 12), command=exit)  #Used to properly close the program
        self.button_exit.pack(side="left", padx=10)
  
    def run(self):
        self.welcome.mainloop()  #Keeps program running