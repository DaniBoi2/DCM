import tkinter as tk
from login import login_file

def end_this_file():  #Function to close this welcome window and open login screen
    welcome_window.withdraw()
    login_file()  #Go to login file

welcome_window = tk.Tk()
welcome_window.title("Welcome!")
welcome_window.geometry("300x100")
welcome_window.resizable(False, False)    #Make window non-resizable 

# Create a top label
top_label = tk.Label(welcome_window, text="Welcome to the GUI Interface")
top_label.pack()

# Create a button to proceed
button_proceed = tk.Button(welcome_window, text="Proceed to Login/Registration",command=end_this_file)
button_proceed.pack()

# Run the Tkinter main loop
welcome_window.mainloop()  

