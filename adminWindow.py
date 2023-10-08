import tkinter as tk
from tkinter import *
import json

def admin_file():
    def delete_user_data():
        user_data_file = r"data_files\Users.json"
        backup_file = r"data_files\backup.txt"

        with open(user_data_file, "r") as user_file:  #Open in read mode
            user_items = json.load(user_file)  # Load json file and read contents
        with open(backup_file, "a") as backup_file:  #Save contents to backup txt file, appends to everything else
            for user in user_items:
                backup_file.write(json.dumps(user) + "\n")
        with open(user_data_file, "w") as user_file:  #Open json file in write mode to delete everything
            user_file.write("[]")  #Write empty json array so it can be appended through registration

        label_bottom.config(text="All data has been deleted!")  
        button_delete.config(state="disabled")      
        
    admin_page = tk.Tk()
    admin_page.title("Admin Settings")
    admin_page.geometry("400x100")
    admin_page.resizable(False, False)

    # Create a top label
    top_label = tk.Label(admin_page, text="Would you like to delete all saved user data?")
    top_label.pack()

    #Create a delete bottom
    button_delete = tk.Button(admin_page, text="Delete All User Data", command=delete_user_data)
    button_delete.pack()

    #Create a bottom label
    label_bottom = tk.Label(admin_page, text="")
    label_bottom.pack()

    admin_page.mainloop()