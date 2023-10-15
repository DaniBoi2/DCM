import tkinter as tk
from tkinter import *
import json
import os

class MainScreen:
    def __init__(self, filename, x_offset, y_offset, welcome):
        self.filename = filename
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.welcome = welcome

    def main_screen(self,user_name): #Main screen pops up, user_name as input so it can display "Logged in as [user_name]" 
        
        with open(self.filename, 'r') as file:
            users = json.load(file)

            
            user_data = None
            for user_dict in users:
               
                if user_dict["name"] == user_name:
                    user_data = user_dict
                    serial_num = user_dict["SerialNum"]
                    break

            
            user = user_data
            print(user)

        def logout(): 
            main_window.withdraw()  #At logout, hide main screen window and show welcome screen again
            self.welcome.deiconify()

        main_window = tk.Tk()
        main_window.title("Pacemaker Control Platform")
        main_window.geometry(f"1200x400+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        main_window.resizable(False, False)
        label_topLeft =tk.Label(main_window, text="Logged in as " + user_name + ",  Serial Number: " + str(serial_num))
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

        bad_param = tk.Label(main_window, text = " ")
        bad_param.grid(row = 6, column = 5)

        def save_state(user_name):
             # Load the existing user data from the JSON file.
            with open(self.filename, 'r') as file:
             users = json.load(file)

    # Find the user with the matching username.
            for user in users:
                if user['name'] == user_name:
                    flag = True
                    bad_param.config(text = " ")

                    #AAO Limit checker
                    if(float(entry_LRL_AAO.get()) < 30 or float(entry_LRL_AAO.get()) > 175 ):
                        bad_param.config(text = "AAO Lower Rate Limit is out of range")
                        flag = False

                    if(float(entry_URL_AAO.get()) < 50 or float(entry_URL_AAO.get()) > 175 ):
                        bad_param.config(text = "AAO Upper Rate Limit is out of range")
                        flag = False

                    if(float(entry_AA_AAO.get()) != 0 and (float(entry_AA_AAO.get()) < 0.5 or float(entry_AA_AAO.get()) > 3.2) and (float(entry_AA_AAO.get()) < 3.5 or float(entry_AA_AAO.get()) > 7.0)):
                        bad_param.config(text = "AAO Atrial Amplitude is out of range")
                        flag = False

                    if(float(entry_APW_AAO.get()) != 0.05 and (float(entry_APW_AAO.get()) < 0.1 or float(entry_APW_AAO.get()) > 1.9 )):
                        bad_param.config(text = "AAO Atrial Pulse Width is out of range")
                        flag = False

                    #AAI Limit Checker
                    if(float(entry_LRL_AAI.get()) < 30 or float(entry_LRL_AAI.get()) > 175 ):
                        bad_param.config(text = "AAI Lower Rate Limit is out of range")
                        flag = False

                    if(float(entry_URL_AAI.get()) < 50 or float(entry_URL_AAI.get()) > 175 ):
                        bad_param.config(text = "AAI Upper Rate Limit is out of range")
                        flag = False

                    if(float(entry_AA_AAI.get()) != 0 and (float(entry_AA_AAI.get()) < 0.5 or float(entry_AA_AAI.get()) > 3.2) and (float(entry_AA_AAI.get()) < 3.5 or float(entry_AA_AAI.get()) > 7.0)):
                        bad_param.config(text = "AAI Atrial Amplitude is out of range")
                        flag = False

                    if(float(entry_APW_AAI.get()) != 0.05 and (float(entry_APW_AAI.get()) < 0.1 or float(entry_APW_AAI.get()) > 1.9 )):
                        bad_param.config(text = "AAI Atrial Pulse Width is out of range")
                        flag = False

                    if(float(entry_AS_AAI.get()) != 0.25 and float(entry_AS_AAI.get()) != 0.50 and float(entry_AS_AAI.get()) != 0.75 and (float(entry_AS_AAI.get()) < 1  or float(entry_AS_AAI.get()) > 10)):
                        bad_param.config(text = "AAI Atrial Sensitivity is out of range")
                        flag = False

                    if(float(entry_ARP_AAI.get()) < 150 or float(entry_ARP_AAI.get()) > 500 ):
                        bad_param.config(text = "AAI ARP is out of range")
                        flag = False

                    if(float(entry_PVARP_AAI.get()) < 150 or float(entry_PVARP_AAI.get()) > 500 ):
                        bad_param.config(text = "AAI PVARP is out of range")
                        flag = False

                    

                    if(float(entry_H_AAI.get()) != 0 and (float(entry_H_AAI.get()) < 30 or float(entry_H_AAI.get()) > 175 )):
                        bad_param.config(text = "AAI Hysteresis is out of range")
                        flag = False

                    #VOO Limit Checker
                    if(float(entry_LRL_VOO.get()) < 30 or float(entry_LRL_VOO.get()) > 175 ):
                        bad_param.config(text = "VOO Lower Rate Limit is out of range")
                        flag = False

                    if(float(entry_URL_VOO.get()) < 50 or float(entry_URL_VOO.get()) > 175 ):
                        bad_param.config(text = "VOO Upper Rate Limit is out of range")
                        flag = False

                    if(float(entry_VA_VOO.get()) != 0 and (float(entry_VA_VOO.get()) < 0.5 or float(entry_VA_VOO.get()) > 3.2) and (float(entry_VA_VOO.get()) < 3.5 or float(entry_VA_VOO.get()) > 7.0) ):
                        bad_param.config(text = "VOO Ventricular Amplitude is out of range")
                        flag = False

                    if(float(entry_VPW_VOO.get()) != 0.05 and (float(entry_VPW_VOO.get()) < 0.1 or float(entry_VPW_VOO.get()) > 1.9 )):
                        bad_param.config(text = "VOO Ventricular Pulse Width is out of range")
                        flag = False


                    #VII Limit Checker
                    if(float(entry_LRL_VVI.get()) < 30 or float(entry_LRL_VVI.get()) > 175 ):
                        bad_param.config(text = "VVI Lower Rate Limit is out of range")
                        flag = False

                    if(float(entry_URL_VVI.get()) < 50 or float(entry_URL_VVI.get()) > 175 ):
                        bad_param.config(text = "VVI Upper Rate Limit is out of range")
                        flag = False

                    if(float(entry_VA_VVI.get()) != 0 and (float(entry_VA_VVI.get()) < 0.5 or float(entry_VA_VVI.get()) > 3.2) and (float(entry_VA_VVI.get()) < 3.5 or float(entry_VA_VVI.get()) > 7.0) ):
                        bad_param.config(text = "VVI Ventricular Amplitude is out of range")
                        flag = False

                    if(float(entry_VPW_VVI.get()) != 0.05 and (float(entry_VPW_VVI.get()) < 0.1 or float(entry_VPW_VVI.get()) > 1.9 )):
                        bad_param.config(text = "VVI Ventricular Pulse Width is out of range")
                        flag = False

                    if(float(entry_VS_VVI.get()) != 0.25 and float(entry_VS_VVI.get()) != 0.50 and float(entry_VS_VVI.get()) != 0.75 and (float(entry_VS_VVI.get()) < 1  or float(entry_VS_VVI.get()) > 10)):
                        bad_param.config(text = "VVI Ventricular Sensitivity is out of range")
                        flag = False

                    if(float(entry_VRP_VVI.get()) < 150 or float(entry_VRP_VVI.get()) > 500 ):
                        bad_param.config(text = "VVI VRP is out of range")
                        flag = False

                    
                    if(float(entry_RS_VVI.get()) != 0 and float(entry_RS_VVI.get()) != 3 and float(entry_RS_VVI.get()) != 6 and float(entry_RS_VVI.get()) != 9 and float(entry_RS_VVI.get()) != 12 and float(entry_RS_VVI.get()) != 15 and float(entry_RS_VVI.get()) != 18 and float(entry_RS_VVI.get()) != 21 and float(entry_RS_VVI.get()) != 25):
                        bad_param.config(text = "VVI Rate Smoothing is out of range")
                        flag = False

                    if(float(entry_H_VVI.get()) != 0 and (float(entry_H_VVI.get()) < 30 or float(entry_H_VVI.get()) > 175 )):
                        bad_param.config(text = "VVI Hysteresis is out of range")
                        flag = False

                    # Update the 'parameters' field with the parameter values from the app.
                    if flag:
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