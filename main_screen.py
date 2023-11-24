import tkinter as tk
from tkinter import *
import json
import os

class MainScreen:
    def __init__(self, filename, x_offset, y_offset, welcome):
        self.filename = filename
        self.x_offset = 20
        self.y_offset = 20
        self.welcome = welcome
        self.connection_flag = False
        self.egramX = []
        self.egramY = []

    def main_screen(self,user_name): #Main screen pops up, user_name as input so it can display "Logged in as [user_name]" 
        def logout(): 
            main_window.withdraw()  #At logout, hide main screen window and show welcome screen again
            self.welcome.deiconify()

        def connection():
            if (self.connection_flag == False):
                self.connection_flag = True
                button_connect.config(text="Disconnect")
                label_connection.config(text="Currently Connected")
            else:
                self.connection_flag = False
                button_connect.config(text="Connect")
                label_connection.config(text="Currently Disconnected")

        with open(self.filename, 'r') as file:
            users = json.load(file)
            user = None
            for user_dict in users:
                if user_dict["name"] == user_name:
                    user = user_dict
                    serial_num = user_dict["SerialNum"]
                    break

        main_window = tk.Tk()
        main_window.title("Pacemaker Control Platform")
        main_window.geometry(f"1300x700+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        main_window.resizable(True, True)
        label_topLeft =tk.Label(main_window, text="Logged in as " + user_name + ",  Serial Number: " + str(serial_num))
        label_topLeft.grid(row=0, column=0, sticky="nw")  # Putting it at top left
        label_top =tk.Label(main_window, text="Pacemaker Control Platform",font=("Helvetica", 15))
        label_top.grid(row=0, column=1, columnspan=2, sticky="n", pady=(0,10))  # Putting it at top
        button_logout = tk.Button(main_window, text="Logout", command=logout)
        button_logout.grid(row=0, column=5, sticky="n")
        button_connect = tk.Button(main_window, text="Connect", command=connection)
        button_connect.grid(row=3, column=5, sticky="s")
        label_connection = tk.Label(main_window, text="Currently Disconnected", wraplength=75)
        label_connection.grid(row=4, column=5, sticky="n")
        label_state = tk.Label(main_window, text="State")  #Used to show the current state (AOO,VOO...etc)
        label_state.grid(row=2, column=0, sticky="nw")
        bad_param = tk.Label(main_window, text = "", wraplength=150)  #Used to show error msgs
        bad_param.grid(row = 8, column = 5, sticky="n")

        #Entry widgets for AOO
        entry_LRL_AOO = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AOO.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AOO.insert(-1, user["parameters"]["AOO_LRL"]) #Default value of 0
        entry_LRL_AOO.grid_remove()
        entry_URL_AOO = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AOO.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AOO.insert(-1, user["parameters"]["AOO_URL"])  #Default value of 0
        entry_URL_AOO.grid_remove()
        entry_AA_AOO = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AOO.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AOO.insert(-1, user["parameters"]["AOO_AA"])  #Default value of 0
        entry_AA_AOO.grid_remove()
        entry_APW_AOO = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AOO.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AOO.insert(-1, user["parameters"]["AOO_APW"])  #Default value of 0
        entry_APW_AOO.grid_remove()

        #Entry widgets for VOO
        entry_LRL_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VOO.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VOO.insert(-1, user["parameters"]["VOO_LRL"]) #Default value of 0
        entry_LRL_VOO.grid_remove()
        entry_URL_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VOO.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VOO.insert(-1, user["parameters"]["VOO_URL"])  #Default value of 0
        entry_URL_VOO.grid_remove()
        entry_VA_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VOO.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VOO.insert(-1, user["parameters"]["VOO_VA"])  #Default value of 0
        entry_VA_VOO.grid_remove()
        entry_VPW_VOO = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VOO.grid(row=9, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VOO.insert(-1, user["parameters"]["VOO_VPW"])  #Default value of 0
        entry_VPW_VOO.grid_remove()

        #Entry widgets for AAI
        entry_LRL_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AAI.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AAI.insert(-1, user["parameters"]["AAI_LRL"]) #Default value of 0
        entry_LRL_AAI.grid_remove()
        entry_URL_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AAI.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AAI.insert(-1, user["parameters"]["AAI_URL"])  #Default value of 0
        entry_URL_AAI.grid_remove()
        entry_AA_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AAI.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AAI.insert(-1, user["parameters"]["AAI_AA"])  #Default value of 0
        entry_AA_AAI.grid_remove()
        entry_APW_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AAI.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AAI.insert(-1, user["parameters"]["AAI_APW"])  #Default value of 0
        entry_APW_AAI.grid_remove()
        entry_AS_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_AS_AAI.grid(row=4, column=3, pady=(20, 10), padx=(5,0), sticky="w")
        entry_AS_AAI.insert(-1, user["parameters"]["AAI_AS"])  #Default value of 0
        entry_AS_AAI.grid_remove()
        entry_ARP_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_ARP_AAI.grid(row=5, column=3, pady=10, padx=(5,0), sticky="w")
        entry_ARP_AAI.insert(-1, user["parameters"]["AAI_ARP"])  #Default value of 0
        entry_ARP_AAI.grid_remove()
        entry_PVARP_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_PVARP_AAI.grid(row=7, column=3, pady=10, padx=(5,0), sticky="w")
        entry_PVARP_AAI.insert(-1, user["parameters"]["AAI_PVARP"])  #Default value of 0
        entry_PVARP_AAI.grid_remove()
        entry_H_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_H_AAI.grid(row=8, column=3, pady=10, padx=(5,0), sticky="w")
        entry_H_AAI.insert(-1, user["parameters"]["AAI_H"])  #Default value of 0
        entry_H_AAI.grid_remove()
        entry_RS_AAI = tk.Entry(main_window, width=8, justify="center")
        entry_RS_AAI.grid(row=9, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RS_AAI.insert(-1, user["parameters"]["AAI_RS"])  #Default value of 0
        entry_RS_AAI.grid_remove()

        #Entry widgets for VVI
        entry_LRL_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VVI.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VVI.insert(-1, user["parameters"]["VVI_LRL"]) #Default value of 0
        entry_LRL_VVI.grid_remove()
        entry_URL_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VVI.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VVI.insert(-1, user["parameters"]["VVI_URL"])  #Default value of 0
        entry_URL_VVI.grid_remove()
        entry_VA_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VVI.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VVI.insert(-1, user["parameters"]["VVI_VA"])  #Default value of 0
        entry_VA_VVI.grid_remove()
        entry_VPW_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VVI.grid(row=9, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VVI.insert(-1, user["parameters"]["VVI_VPW"])  #Default value of 0
        entry_VPW_VVI.grid_remove()
        entry_VS_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VS_VVI.grid(row=10, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VS_VVI.insert(-1, user["parameters"]["VVI_VS"])  #Default value of 0
        entry_VS_VVI.grid_remove()
        entry_VRP_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_VRP_VVI.grid(row=6, column=3, pady=10, padx=(5,0), sticky="w")
        entry_VRP_VVI.insert(-1, user["parameters"]["VVI_VRP"])  #Default value of 0
        entry_VRP_VVI.grid_remove()
        entry_H_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_H_VVI.grid(row=8, column=3, pady=10, padx=(5,0), sticky="w")
        entry_H_VVI.insert(-1, user["parameters"]["VVI_H"])  #Default value of 0
        entry_H_VVI.grid_remove()
        entry_RS_VVI = tk.Entry(main_window, width=8, justify="center")
        entry_RS_VVI.grid(row=9, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RS_VVI.insert(-1, user["parameters"]["VVI_RS"])  #Default value of 0
        entry_RS_VVI.grid_remove()


        
        #Entry widgets for AOOR
        entry_LRL_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AOOR.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AOOR.insert(-1, user["parameters"]["AOOR_LRL"]) #Default value of 0
        entry_LRL_AOOR.grid_remove()

        
        entry_URL_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AOOR.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AOOR.insert(-1, user["parameters"]["AOOR_URL"])  #Default value of 0
        entry_URL_AOOR.grid_remove()
        # ADD NEW ROW AND COL
        entry_MSR_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_MSR_AOOR.grid(row=10, column=3, pady=10, padx=(5,0), sticky="w")
        entry_MSR_AOOR.insert(-1, user["parameters"]["AOOR_MSR"])  #Default value of 0
        entry_MSR_AOOR.grid_remove()

        entry_AA_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AOOR.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AOOR.insert(-1, user["parameters"]["AOOR_AA"])  #Default value of 0
        entry_AA_AOOR.grid_remove()

        entry_APW_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AOOR.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AOOR.insert(-1, user["parameters"]["AOOR_APW"])  #Default value of 0
        entry_APW_AOOR.grid_remove()

        entry_AT_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_AT_AOOR.grid(row=11, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AT_AOOR.insert(-1, user["parameters"]["AOOR_AT"])  #Default value of 0
        entry_AT_AOOR.grid_remove()

        entry_RT_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RT_AOOR.grid(row=12, column=1, pady=10, padx=(5,0), sticky="w")
        entry_RT_AOOR.insert(-1, user["parameters"]["AOOR_RT"])  #Default value of 0
        entry_RT_AOOR.grid_remove()

        entry_RF_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RF_AOOR.grid(row=11, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RF_AOOR.insert(-1, user["parameters"]["AOOR_RF"])  #Default value of 0
        entry_RF_AOOR.grid_remove()

        entry_RTI_AOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RTI_AOOR.grid(row=12, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RTI_AOOR.insert(-1, user["parameters"]["AOOR_RTI"])  #Default value of 0
        entry_RTI_AOOR.grid_remove()

        # Entry widgets for AAIR
        entry_LRL_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_AAIR.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_AAIR.insert(-1, user["parameters"]["AAIR_LRL"]) #Default value of 0
        entry_LRL_AAIR.grid_remove()

        
        entry_URL_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_URL_AAIR.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_AAIR.insert(-1, user["parameters"]["AAIR_URL"])  #Default value of 0
        entry_URL_AAIR.grid_remove()
        
        entry_MSR_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_MSR_AAIR.grid(row=10, column=3, pady=10, padx=(5,0), sticky="w")
        entry_MSR_AAIR.insert(-1, user["parameters"]["AAIR_MSR"])  #Default value of 0
        entry_MSR_AAIR.grid_remove()

        entry_AA_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_AA_AAIR.grid(row=6, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AA_AAIR.insert(-1, user["parameters"]["AAIR_AA"])  #Default value of 0
        entry_AA_AAIR.grid_remove()

        entry_APW_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_APW_AAIR.grid(row=7, column=1, pady=10, padx=(5,0), sticky="w")
        entry_APW_AAIR.insert(-1, user["parameters"]["AAIR_APW"])  #Default value of 0
        entry_APW_AAIR.grid_remove()

        # add 4 more here
        entry_AS_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_AS_AAIR.grid(row=4, column=3, pady=(20, 10), padx=(5,0), sticky="w")
        entry_AS_AAIR.insert(-1, user["parameters"]["AAIR_AS"])  #Default value of 0
        entry_AS_AAIR.grid_remove()

        entry_ARP_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_ARP_AAIR.grid(row=5, column=3, pady=10, padx=(5,0), sticky="w")
        entry_ARP_AAIR.insert(-1, user["parameters"]["AAIR_ARP"])  #Default value of 0
        entry_ARP_AAIR.grid_remove()

        entry_PVARP_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_PVARP_AAIR.grid(row=7, column=3, pady=10, padx=(5,0), sticky="w")
        entry_PVARP_AAIR.insert(-1, user["parameters"]["AAIR_PVARP"])  #Default value of 0
        entry_PVARP_AAIR.grid_remove()

        entry_AT_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_AT_AAIR.grid(row=11, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AT_AAIR.insert(-1, user["parameters"]["AAIR_AT"])  #Default value of 0
        entry_AT_AAIR.grid_remove()

        entry_RT_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_RT_AAIR.grid(row=12, column=1, pady=10, padx=(5,0), sticky="w")
        entry_RT_AAIR.insert(-1, user["parameters"]["AAIR_RT"])  #Default value of 0
        entry_RT_AAIR.grid_remove()

        entry_RF_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_RF_AAIR.grid(row=11, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RF_AAIR.insert(-1, user["parameters"]["AAIR_RF"])  #Default value of 0
        entry_RF_AAIR.grid_remove()

        entry_RTI_AAIR = tk.Entry(main_window, width=8, justify="center")
        entry_RTI_AAIR.grid(row=12, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RTI_AAIR.insert(-1, user["parameters"]["AAIR_RTI"])  #Default value of 0
        entry_RTI_AAIR.grid_remove()

        # entry widgets for VOOR

        entry_LRL_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VOOR.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VOOR.insert(-1, user["parameters"]["VOOR_LRL"]) #Default value of 0
        entry_LRL_VOOR.grid_remove()

        
        entry_URL_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VOOR.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VOOR.insert(-1, user["parameters"]["VOOR_URL"])  #Default value of 0
        entry_URL_VOOR.grid_remove()
        
        entry_MSR_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_MSR_VOOR.grid(row=10, column=3, pady=10, padx=(5,0), sticky="w")
        entry_MSR_VOOR.insert(-1, user["parameters"]["VOOR_MSR"])  #Default value of 0
        entry_MSR_VOOR.grid_remove()

        entry_VA_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VOOR.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VOOR.insert(-1, user["parameters"]["VOOR_VA"])  #Default value of 0
        entry_VA_VOOR.grid_remove()

        entry_VPW_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VOOR.grid(row=9, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VOOR.insert(-1, user["parameters"]["VOOR_VPW"])  #Default value of 0
        entry_VPW_VOOR.grid_remove()

        entry_AT_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_AT_VOOR.grid(row=11, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AT_VOOR.insert(-1, user["parameters"]["VOOR_AT"])  #Default value of 0
        entry_AT_VOOR.grid_remove()

        entry_RT_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RT_VOOR.grid(row=12, column=1, pady=10, padx=(5,0), sticky="w")
        entry_RT_VOOR.insert(-1, user["parameters"]["VOOR_RT"])  #Default value of 0
        entry_RT_VOOR.grid_remove()

        entry_RF_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RF_VOOR.grid(row=11, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RF_VOOR.insert(-1, user["parameters"]["VOOR_RF"])  #Default value of 0
        entry_RF_VOOR.grid_remove()

        entry_RTI_VOOR = tk.Entry(main_window, width=8, justify="center")
        entry_RTI_VOOR.grid(row=12, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RTI_VOOR.insert(-1, user["parameters"]["VOOR_RTI"])  #Default value of 0
        entry_RTI_VOOR.grid_remove()

        # entry widgets for VVIR

        entry_LRL_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_LRL_VVIR.grid(row=4, column=1, pady=(20,10), padx=(5,0), sticky="w")
        entry_LRL_VVIR.insert(-1, user["parameters"]["VVIR_LRL"]) #Default value of 0
        entry_LRL_VVIR.grid_remove()

        
        entry_URL_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_URL_VVIR.grid(row=5, column=1, pady=10, padx=(5,0), sticky="w")
        entry_URL_VVIR.insert(-1, user["parameters"]["VVIR_URL"])  #Default value of 0
        entry_URL_VVIR.grid_remove()
        
        entry_MSR_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_MSR_VVIR.grid(row=10, column=3, pady=10, padx=(5,0), sticky="w")
        entry_MSR_VVIR.insert(-1, user["parameters"]["VVIR_MSR"])  #Default value of 0
        entry_MSR_VVIR.grid_remove()

        entry_VA_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_VA_VVIR.grid(row=8, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VA_VVIR.insert(-1, user["parameters"]["VVIR_VA"])  #Default value of 0
        entry_VA_VVIR.grid_remove()

        entry_VPW_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_VPW_VVIR.grid(row=9, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VPW_VVIR.insert(-1, user["parameters"]["VVIR_VPW"])  #Default value of 0
        entry_VPW_VVIR.grid_remove()


        entry_VS_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_VS_VVIR.grid(row=10, column=1, pady=10, padx=(5,0), sticky="w")
        entry_VS_VVIR.insert(-1, user["parameters"]["VVIR_VS"])  #Default value of 0
        entry_VS_VVIR.grid_remove()

        entry_VRP_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_VRP_VVIR.grid(row=6, column=3, pady=10, padx=(5,0), sticky="w")
        entry_VRP_VVIR.insert(-1, user["parameters"]["VVIR_VRP"])  #Default value of 0
        entry_VRP_VVIR.grid_remove()

        entry_AT_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_AT_VVIR.grid(row=11, column=1, pady=10, padx=(5,0), sticky="w")
        entry_AT_VVIR.insert(-1, user["parameters"]["VVIR_AT"])  #Default value of 0
        entry_AT_VVIR.grid_remove()

        entry_RT_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_RT_VVIR.grid(row=12, column=1, pady=10, padx=(5,0), sticky="w")
        entry_RT_VVIR.insert(-1, user["parameters"]["VVIR_RT"])  #Default value of 0
        entry_RT_VVIR.grid_remove()

        entry_RF_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_RF_VVIR.grid(row=11, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RF_VVIR.insert(-1, user["parameters"]["VVIR_RF"])  #Default value of 0
        entry_RF_VVIR.grid_remove()

        entry_RTI_VVIR = tk.Entry(main_window, width=8, justify="center")
        entry_RTI_VVIR.grid(row=12, column=3, pady=10, padx=(5,0), sticky="w")
        entry_RTI_VVIR.insert(-1, user["parameters"]["VVIR_RTI"])  #Default value of 0
        entry_RTI_VVIR.grid_remove()
        
    
        def update_state_widgets(state_label_text, *widgets_to_remove):
            label_state.config(text=f"State: {state_label_text}")
            bad_param.config(text=" ")

            for widget in widgets_to_remove:
                widget.grid_remove()

        def update_state_entries(entries_to_show):
            for entry in entries_to_show:
                entry.grid()

        widgets = [entry_LRL_AOO, entry_URL_AOO, entry_AA_AOO, entry_APW_AOO, 
        entry_LRL_VOO, entry_URL_VOO, entry_VA_VOO, entry_VPW_VOO, 
        entry_LRL_AAI, entry_URL_AAI, entry_AA_AAI, entry_APW_AAI,
        entry_AS_AAI, entry_ARP_AAI, entry_PVARP_AAI, entry_H_AAI,
        entry_RS_AAI, entry_LRL_VVI, entry_URL_VVI, entry_VA_VVI, entry_VPW_VVI,
        entry_VS_VVI, entry_VRP_VVI, entry_H_VVI, entry_RS_VVI, entry_LRL_AOOR, entry_URL_AOOR, entry_MSR_AOOR, entry_AA_AOOR, entry_APW_AOOR,
        entry_AT_AOOR, entry_RT_AOOR, entry_RF_AOOR, entry_RTI_AOOR, 
        entry_LRL_AAIR, entry_URL_AAIR, entry_MSR_AAIR, entry_AA_AAIR, entry_APW_AAIR,
        entry_AS_AAIR, entry_ARP_AAIR, entry_PVARP_AAIR, 
        entry_AT_AAIR, entry_RT_AAIR, entry_RF_AAIR, entry_RTI_AAIR, 
        entry_LRL_VOOR,
        entry_URL_VOOR,
        entry_MSR_VOOR,
        entry_VA_VOOR,
        entry_VPW_VOOR,
        entry_AT_VOOR,
        entry_RT_VOOR,
        entry_RF_VOOR,
        entry_RTI_VOOR, entry_LRL_VVIR,
                entry_URL_VVIR,
                entry_MSR_VVIR,
                entry_VA_VVIR,
                entry_VPW_VVIR,
                entry_VS_VVIR,
                entry_VRP_VVIR,
                entry_AT_VVIR,
                entry_RT_VVIR,
                entry_RF_VVIR,
                entry_RTI_VVIR]

        def AOO_pressed():
            update_state_widgets("AOO", *widgets)
            update_state_entries([entry_LRL_AOO, entry_URL_AOO, entry_AA_AOO, entry_APW_AOO])

        def VOO_pressed():
            update_state_widgets("VOO", *widgets)
            update_state_entries([entry_LRL_VOO, entry_URL_VOO, entry_VA_VOO, entry_VPW_VOO])

        def AAI_pressed():
            update_state_widgets("AAI", *widgets)
            update_state_entries([entry_LRL_AAI, entry_URL_AAI, entry_AA_AAI, entry_APW_AAI,
                                entry_AS_AAI, entry_ARP_AAI, entry_PVARP_AAI, entry_H_AAI,
                                entry_RS_AAI])

        def VVI_pressed():
            update_state_widgets("VVI", *widgets)
            update_state_entries([entry_LRL_VVI, entry_URL_VVI, entry_VA_VVI, entry_VPW_VVI,
                                entry_VS_VVI, entry_VRP_VVI, entry_H_VVI, entry_RS_VVI])

        def AOOR_pressed():
            update_state_widgets("AOOR", *widgets)
            update_state_entries([entry_LRL_AOOR, entry_URL_AOOR, entry_MSR_AOOR, entry_AA_AOOR, entry_APW_AOOR,
                                entry_AT_AOOR, entry_RT_AOOR, entry_RF_AOOR, entry_RTI_AOOR])

        def AAIR_pressed():
            update_state_widgets("AAIR", *widgets)
            update_state_entries([entry_LRL_AAIR, entry_URL_AAIR, entry_MSR_AAIR, entry_AA_AAIR, entry_APW_AAIR,
                                 entry_AS_AAIR, entry_ARP_AAIR, entry_PVARP_AAIR, 
                                entry_AT_AAIR, entry_RT_AAIR, entry_RF_AAIR, entry_RTI_AAIR])

        def VOOR_pressed():
            update_state_widgets("VOOR", *widgets)
            update_state_entries([entry_LRL_VOOR,
                entry_URL_VOOR,
                entry_MSR_VOOR,
                entry_VA_VOOR,
                entry_VPW_VOOR,
                entry_AT_VOOR,
                entry_RT_VOOR,
                entry_RF_VOOR,
                entry_RTI_VOOR])

        def VVIR_pressed():
            update_state_widgets("VVIR", *widgets)
            update_state_entries([entry_LRL_VVIR,
                entry_URL_VVIR,
                entry_MSR_VVIR,
                entry_VA_VVIR,
                entry_VPW_VVIR,
                entry_VS_VVIR,
                entry_VRP_VVIR,
                entry_AT_VVIR,
                entry_RT_VVIR,
                entry_RF_VVIR,
                entry_RTI_VVIR])


        def save_state(user_name): 
            def valid_number(number_input):   #Function created to check valid integer numbers and float number inputs
                decimal_point_count = 0
                for char in number_input:
                    if char.isdigit(): continue  #If only integer digits, just keep continuing 
                    elif char == '.' and decimal_point_count == 0: decimal_point_count += 1  #If find decimal point, increment (we can only have 1 decimal point in total)
                    else: return False  #If not integer digit and not decimal, then it must be an invalid digit so return false immediately
                if decimal_point_count == 1 and number_input[0] == '.': return False # Ensure there is at least one digit in the string
                return True   #Otherwise return true
            
            with open(self.filename, 'r') as file: users = json.load(file)  # Load the existing user data from the JSON file.
            for user in users:   # Find the user with the matching username
                if user['name'] == user_name:
                    flag = True  #Default value meaning that data should be saved
                    bad_param.config(text = " ")
                    
                    if (label_state.cget("text") == "State: AOO"):  #Get current state
                        if (valid_number(entry_LRL_AOO.get()) and valid_number(entry_URL_AOO.get()) and valid_number(entry_AA_AOO.get()) and valid_number(entry_APW_AOO.get())):
                            #AOO Limit checker
                            if(float(entry_LRL_AOO.get()) < 30 or float(entry_LRL_AOO.get()) > 175 ):
                                bad_param.config(text = "AOO Lower Rate Limit is out of range")
                                flag = False
                            if(float(entry_URL_AOO.get()) < 50 or float(entry_URL_AOO.get()) > 175 ):
                                bad_param.config(text = "AOO Upper Rate Limit is out of range")
                                flag = False
                            if(float(entry_AA_AOO.get()) != 0 and (float(entry_AA_AOO.get()) < 0.5 or float(entry_AA_AOO.get()) > 3.2) and (float(entry_AA_AOO.get()) < 3.5 or float(entry_AA_AOO.get()) > 7.0)):
                                bad_param.config(text = "AOO Atrial Amplitude is out of range")
                                flag = False
                            if(float(entry_APW_AOO.get()) != 0.05 and (float(entry_APW_AOO.get()) < 0.1 or float(entry_APW_AOO.get()) > 1.9 )):
                                bad_param.config(text = "AOO Atrial Pulse Width is out of range")
                                flag = False
                        else: #If all numbers are not valid like asked in above condition, then input must be invalid
                            bad_param.config(text = "Invalid Input")
                            flag = False

                    elif (label_state.cget("text") == "State: AAI"):
                        if (valid_number(entry_LRL_AAI.get()) and valid_number(entry_URL_AAI.get()) and valid_number(entry_AA_AAI.get()) and valid_number(entry_APW_AAI.get()) and
                            valid_number(entry_AS_AAI.get()) and valid_number(entry_ARP_AAI.get()) and valid_number(entry_PVARP_AAI.get()) and valid_number(entry_H_AAI.get())):
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
                        else: #If all numbers are not valid like asked in above condition, then input must be invalid
                            bad_param.config(text = "Invalid Input")
                            flag = False

                    elif (label_state.cget("text") == "State: VOO"):  #Get current state
                        if (valid_number(entry_LRL_VOO.get()) and valid_number(entry_URL_VOO.get()) and valid_number(entry_VA_VOO.get()) and valid_number(entry_VPW_VOO.get())):
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
                        else: #If all numbers are not valid like asked in above condition, then input must be invalid
                            bad_param.config(text = "Invalid Input")
                            flag = False

                    elif (label_state.cget("text") == "State: VVI"):
                        if (valid_number(entry_LRL_VVI.get()) and valid_number(entry_URL_VVI.get()) and valid_number(entry_VA_VVI.get()) and valid_number(entry_VPW_VVI.get()) and
                            valid_number(entry_VS_VVI.get()) and valid_number(entry_VRP_VVI.get()) and valid_number(entry_RS_VVI.get()) and valid_number(entry_H_VVI.get())):
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
                        else: #If all numbers are not valid like asked in above condition, then input must be invalid
                                bad_param.config(text = "Invalid Input")
                                flag = False

                    
                    elif (label_state.cget("text") == "State: AOOR"):

                        if (valid_number(entry_LRL_AOOR.get()) and valid_number(entry_URL_AOOR.get()) and valid_number(entry_MSR_AOOR.get()) and valid_number(entry_AA_AOOR.get()) and valid_number(entry_APW_AOOR.get()) and
                            valid_number(entry_AT_AOOR.get()) and valid_number(entry_RF_AOOR.get()) and valid_number(entry_RT_AOOR.get()) and valid_number(entry_RTI_AOOR.get())):
                            
                            
                            #VII Limit Checker
                            if(float(entry_LRL_AOOR.get()) < 30 or float(entry_LRL_AOOR.get()) > 175 ):
                                bad_param.config(text = "AOOR Lower Rate Limit is out of range")
                                flag = False
                            if(float(entry_URL_AOOR.get()) < 50 or float(entry_URL_AOOR.get()) > 175 ):
                                bad_param.config(text = "AOOR Upper Rate Limit is out of range")
                                flag = False
                            if(float(entry_MSR_AOOR.get()) < 50 or float(entry_MSR_AOOR.get()) > 175):
                                bad_param.config(text = "AOOR Maximum Sensor Rate is out of range")
                                flag = False
                            if(float(entry_AA_AOOR.get()) != 0 and (float(entry_AA_AOOR.get()) < 0.5 or float(entry_AA_AOOR.get()) > 3.2) and (float(entry_AA_AOOR.get()) < 3.5 or float(entry_AA_AOOR.get()) > 7.0)):
                                bad_param.config(text = "AOOR Atrial Amplitude is out of range")
                                flag = False
                            if(float(entry_APW_AOOR.get()) != 0.05 and (float(entry_APW_AOOR.get()) < 0.1 or float(entry_APW_AOOR.get()) > 1.9 )):
                                bad_param.config(text = "AOOR Atrial Pulse Width is out of range")
                                flag = False

                            if(float(entry_AT_AOOR.get()) < 150 or float(entry_AT_AOOR.get()) > 500 ):
                                bad_param.config(text = "AOOR Activity Threshold is out of range")
                                flag = False
                            if(float(entry_RF_AOOR.get()) < 1 or float(entry_RF_AOOR.get()) > 16):
                                bad_param.config(text = "AOOR Response Factor is out of range")
                                flag = False
                            if(float(entry_RT_AOOR.get()) < 10 or float(entry_RT_AOOR.get()) > 50 ):
                                bad_param.config(text = "AOOR Reaction Time is out of range")
                                flag = False
                            if(float(entry_RTI_AOOR.get()) < 2 or float(entry_RTI_AOOR.get()) > 16):
                                bad_param.config(text = "AOOR Recovery Time is out of range")
                                flag = False

                    elif (label_state.cget("text") == "State: AAIR"):
                        if (valid_number(entry_LRL_AAIR.get()) and valid_number(entry_URL_AAIR.get()) and valid_number(entry_MSR_AAIR.get()) and valid_number(entry_AA_AAIR.get()) and valid_number(entry_APW_AAIR.get()) and
                            valid_number(entry_AS_AAIR.get()) and valid_number(entry_ARP_AAIR.get()) and valid_number(entry_PVARP_AAIR.get()) and
                            valid_number(entry_AT_AAIR.get()) and valid_number(entry_RF_AAIR.get()) and valid_number(entry_RT_AAIR.get()) and valid_number(entry_RTI_AAIR.get())):
                            #VII Limit Checker
                            if(float(entry_LRL_AAIR.get()) < 30 or float(entry_LRL_AAIR.get()) > 175 ):
                                bad_param.config(text = "AAIR Lower Rate Limit is out of range")
                                flag = False
                            if(float(entry_URL_AAIR.get()) < 50 or float(entry_URL_AAIR.get()) > 175 ):
                                bad_param.config(text = "AAIR Upper Rate Limit is out of range")
                                flag = False
                            if(float(entry_MSR_AAIR.get())  < 50 or float(entry_MSR_AAIR.get()) > 175):
                                bad_param.config(text = "AAIR Maximum Sensor Rate is out of range")
                                flag = False
                            if(float(entry_AA_AAIR.get()) != 0 and (float(entry_AA_AAIR.get()) < 0.5 or float(entry_AA_AAIR.get()) > 3.2) and (float(entry_AA_AAIR.get()) < 3.5 or float(entry_AA_AAIR.get()) > 7.0)):
                                bad_param.config(text = "AAIR Atrial Amplitude is out of range")
                                flag = False
                            if(float(entry_APW_AAIR.get()) != 0.05 and (float(entry_APW_AAIR.get()) < 0.1 or float(entry_APW_AAIR.get()) > 1.9 )):
                                bad_param.config(text = "AAIR Atrial Pulse Width is out of range")
                                flag = False

                                
                            if(float(entry_AS_AAIR.get()) != 0.25 and float(entry_AS_AAIR.get()) != 0.50 and float(entry_AS_AAIR.get()) != 0.75 and (float(entry_AS_AAIR.get()) < 1  or float(entry_AS_AAIR.get()) > 10)):
                                bad_param.config(text = "AAIR Atrial Sensitivity is out of range")
                                flag = False
                            if(float(entry_ARP_AAIR.get()) < 150 and float(entry_ARP_AAIR.get()) > 500):
                                bad_param.config(text = "AAIR ARP is out of range")
                                flag = False
                            if(float(entry_PVARP_AAIR.get()) < 150 and float(entry_PVARP_AAIR.get()) > 500):
                                bad_param.config(text = "AAIR PVARP is out of range")
                                flag = False

                            if(float(entry_AT_AAIR.get()) < 150 or float(entry_AT_AAIR.get()) > 500 ):
                                bad_param.config(text = "AAIR Activity Threshold is out of range")
                                flag = False
                            if(float(entry_RF_AAIR.get()) < 1 or float(entry_RF_AAIR.get()) > 16):
                                bad_param.config(text = "AAIR Response Factor is out of range")
                                flag = False
                            if(float(entry_RT_AAIR.get()) < 10 or float(entry_RT_AAIR.get()) > 50 ):
                                bad_param.config(text = "AAIR Reaction Time is out of range")
                                flag = False
                            if(float(entry_RTI_AAIR.get()) < 2 or float(entry_RTI_AAIR.get()) > 16):
                                bad_param.config(text = "AAIR Recovery Time is out of range")
                                flag = False

                    # VOOR
                    elif (label_state.cget("text") == "State: VOOR"):
                        if (valid_number(entry_LRL_VOOR.get()) and valid_number(entry_URL_VOOR.get()) and valid_number(entry_MSR_VOOR.get()) and valid_number(entry_VA_VOOR.get()) and valid_number(entry_VPW_VOOR.get()) and
                            valid_number(entry_AT_VOOR.get()) and valid_number(entry_RF_VOOR.get()) and valid_number(entry_RT_VOOR.get()) and valid_number(entry_RTI_VOOR.get())):
                            #VII Limit Checker
                            if(float(entry_LRL_VOOR.get()) < 30 or float(entry_LRL_VOOR.get()) > 175 ):
                                bad_param.config(text = "VOOR Lower Rate Limit is out of range")
                                flag = False
                            if(float(entry_URL_VOOR.get()) < 50 or float(entry_URL_VOOR.get()) > 175 ):
                                bad_param.config(text = "VOOR Upper Rate Limit is out of range")
                                flag = False
                            if(float(entry_MSR_VOOR.get())  < 50 or float(entry_MSR_VOOR.get()) > 175):
                                bad_param.config(text = "VOOR Maximum Sensor Rate is out of range")
                                flag = False

                            if(float(entry_VA_VOOR.get()) != 0 and (float(entry_VA_VOOR.get()) < 0.5 or float(entry_VA_VOOR.get()) > 3.2) and (float(entry_VA_VOOR.get()) < 3.5 or float(entry_VA_VOOR.get()) > 7.0)):
                                bad_param.config(text = "VOOR Ventricular Amplitude is out of range")
                                flag = False
                            if(float(entry_VPW_VOOR.get()) != 0.05 and (float(entry_VPW_VOOR.get()) < 0.1 or float(entry_VPW_VOOR.get()) > 1.9 )):
                                bad_param.config(text = "VOOR Ventricular Pulse Width is out of range")
                                flag = False

                            if(float(entry_AT_VOOR.get()) < 150 or float(entry_AT_VOOR.get()) > 500 ):
                                bad_param.config(text = "VOOR Activity Threshold is out of range")
                                flag = False
                            if(float(entry_RF_VOOR.get()) < 1 or float(entry_RF_VOOR.get()) > 16):
                                bad_param.config(text = "VOOR Response Factor is out of range")
                                flag = False
                            if(float(entry_RT_VOOR.get()) < 10 or float(entry_RT_VOOR.get()) > 50 ):
                                bad_param.config(text = "VOOR Reaction Time is out of range")
                                flag = False
                            if(float(entry_RTI_VOOR.get()) < 2 or float(entry_RTI_VOOR.get()) > 16):
                                bad_param.config(text = "VOOR Recovery Time is out of range")
                                flag = False

                    # VVIR
                    elif (label_state.cget("text") == "State: VVIR"):
                        if (valid_number(entry_LRL_VVIR.get()) and valid_number(entry_URL_VVIR.get()) and valid_number(entry_MSR_VVIR.get()) and valid_number(entry_VA_VVIR.get()) and valid_number(entry_VPW_VVIR.get()) and
                            valid_number(entry_VS_VVIR.get()) and valid_number(entry_VRP_VVIR.get()) and
                            valid_number(entry_AT_VVIR.get()) and valid_number(entry_RF_VVIR.get()) and valid_number(entry_RT_VVIR.get()) and valid_number(entry_RTI_VVIR.get())):
                            #VII Limit Checker
                            if(float(entry_LRL_VVIR.get()) < 30 or float(entry_LRL_VVIR.get()) > 175 ):
                                bad_param.config(text = "VVIR Lower Rate Limit is out of range")
                                flag = False
                            if(float(entry_URL_VVIR.get()) < 50 or float(entry_URL_VVIR.get()) > 175 ):
                                bad_param.config(text = "VVIR Upper Rate Limit is out of range")
                                flag = False
                            if(float(entry_MSR_VVIR.get())  < 50 or float(entry_MSR_VVIR.get()) > 175):
                                bad_param.config(text = "VVIR Maximum Sensor Rate is out of range")
                                flag = False

                            if(float(entry_VA_VVIR.get()) != 0 and (float(entry_VA_VVIR.get()) < 0.5 or float(entry_VA_VVIR.get()) > 3.2) and (float(entry_VA_VVIR.get()) < 3.5 or float(entry_VA_VVIR.get()) > 7.0)):
                                bad_param.config(text = "VVIR Ventricular Amplitude is out of range")
                                flag = False
                            if(float(entry_VPW_VVIR.get()) != 0.05 and (float(entry_VPW_VVIR.get()) < 0.1 or float(entry_VPW_VVIR.get()) > 1.9 )):
                                bad_param.config(text = "VVIR Ventricular Pulse Width is out of range")
                                flag = False

                            if(float(entry_VS_VVIR.get()) != 0.25 and float(entry_VS_VVIR.get()) != 0.50 and float(entry_VS_VVIR.get()) != 0.75 and (float(entry_VS_VVIR.get()) < 1  or float(entry_VS_VVIR.get()) > 10)):
                                bad_param.config(text = "VVIR Ventricular Sensitivity is out of range")
                                flag = False
                            if(float(entry_VRP_VVIR.get()) < 150 or float(entry_VRP_VVIR.get()) > 500 ):
                                bad_param.config(text = "VVIR VRP is out of range")
                                flag = False    

                            if(float(entry_AT_VVIR.get()) < 150 or float(entry_AT_VVIR.get()) > 500 ):
                                bad_param.config(text = "VVIR Activity Threshold is out of range")
                                flag = False
                            if(float(entry_RF_VVIR.get()) < 1 or float(entry_RF_VVIR.get()) > 16):
                                bad_param.config(text = "VVIR Response Factor is out of range")
                                flag = False
                            if(float(entry_RT_VVIR.get()) < 10 or float(entry_RT_VVIR.get()) > 50 ):
                                bad_param.config(text = "VVIR Reaction Time is out of range")
                                flag = False
                            if(float(entry_RTI_VVIR.get()) < 2 or float(entry_RTI_VVIR.get()) > 16):
                                bad_param.config(text = "VVIR Recovery Time is out of range")
                                flag = False

                        else: #If all numbers are not valid like asked in above condition, then input must be invalid
                                bad_param.config(text = "Invalid Input")
                                flag = False
                    else:
                        
                        flag = False  #If none of the states, set to false so nothing gets saved

                    # Update the 'parameters' field with the parameter values, only for the actual state (user could have input invalid values for other states' values)
                    print(flag)
                    if flag:
                        bad_param.config(text="Success!")

                        if label_state.cget("text") == "State: AOO":
                            user['parameters']['AOO_LRL'] = float(entry_LRL_AOO.get())
                            user['parameters']['AOO_URL'] = float(entry_URL_AOO.get())
                            user['parameters']['AOO_AA'] = float(entry_AA_AOO.get())
                            user['parameters']['AOO_APW'] = float(entry_APW_AOO.get())

                        elif label_state.cget("text") == "State: AAI":
                            user['parameters']['AAI_LRL'] = float(entry_LRL_AAI.get())
                            user['parameters']['AAI_URL'] = float(entry_URL_AAI.get())
                            user['parameters']['AAI_AA'] = float(entry_AA_AAI.get())
                            user['parameters']['AAI_APW'] = float(entry_APW_AAI.get())
                            user['parameters']['AAI_AS'] = float(entry_AS_AAI.get())
                            user['parameters']['AAI_ARP'] = float(entry_ARP_AAI.get())
                            user['parameters']['AAI_PVARP'] = float(entry_PVARP_AAI.get())
                            user['parameters']['AAI_RS'] = float(entry_RS_AAI.get())
                            user['parameters']['AAI_H'] = float(entry_H_AAI.get())

                        elif label_state.cget("text") == "State: VOO":
                            user['parameters']['VOO_LRL'] = float(entry_LRL_VOO.get())
                            user['parameters']['VOO_URL'] = float(entry_URL_VOO.get())
                            user['parameters']['VOO_VA'] = float(entry_VA_VOO.get())
                            user['parameters']['VOO_VPW'] = float(entry_VPW_VOO.get())

                        elif label_state.cget("text") == "State: VVI":
                            user['parameters']['VVI_LRL'] = float(entry_LRL_VVI.get())
                            user['parameters']['VVI_URL'] = float(entry_URL_VVI.get())
                            user['parameters']['VVI_VA'] = float(entry_VA_VVI.get())
                            user['parameters']['VVI_VPW'] = float(entry_VPW_VVI.get())
                            user['parameters']['VVI_VS'] = float(entry_VS_VVI.get())
                            user['parameters']['VVI_VRP'] = float(entry_VRP_VVI.get())
                            user['parameters']['VVI_H'] = float(entry_H_VVI.get())
                            user['parameters']['VVI_RS'] = float(entry_RS_VVI.get())

                        elif label_state.cget("text") == "State: AOOR":
                            user['parameters']['AOOR_LRL'] = float(entry_LRL_AOOR.get())
                            user['parameters']['AOOR_URL'] = float(entry_URL_AOOR.get())
                            user['parameters']['AOOR_MSR'] = float(entry_MSR_AOOR.get())
                            user['parameters']['AOOR_AA'] = float(entry_AA_AOOR.get())
                            user['parameters']['AOOR_APW'] = float(entry_APW_AOOR.get())
                            user['parameters']['AOOR_AT'] = float(entry_AT_AOOR.get())
                            user['parameters']['AOOR_RT'] = float(entry_RT_AOOR.get())
                            user['parameters']['AOOR_RF'] = float(entry_RF_AOOR.get())
                            user['parameters']['AOOR_RTI'] = float(entry_RTI_AOOR.get())

                        elif label_state.cget("text") == "State: AAIR":
                            user['parameters']['AAIR_LRL'] = float(entry_LRL_AAIR.get())
                            user['parameters']['AAIR_URL'] = float(entry_URL_AAIR.get())
                            user['parameters']['AAIR_MSR'] = float(entry_MSR_AAIR.get())
                            user['parameters']['AAIR_AA'] = float(entry_AA_AAIR.get())
                            user['parameters']['AAIR_APW'] = float(entry_APW_AAIR.get())
                            user['parameters']['AAIR_AS'] = float(entry_AS_AAIR.get())
                            user['parameters']['AAIR_ARP'] = float(entry_ARP_AAIR.get())
                            user['parameters']['AAIR_PVARP'] = float(entry_PVARP_AAIR.get())
                            user['parameters']['AAIR_AT'] = float(entry_AT_AAIR.get())
                            user['parameters']['AAIR_RT'] = float(entry_RT_AAIR.get())
                            user['parameters']['AAIR_RF'] = float(entry_RF_AAIR.get())
                            user['parameters']['AAIR_RTI'] = float(entry_RTI_AAIR.get())

                        elif label_state.cget("text") == "State: VOOR":
                            user['parameters']['VOOR_LRL'] = float(entry_LRL_VOOR.get())
                            user['parameters']['VOOR_URL'] = float(entry_URL_VOOR.get())
                            user['parameters']['VOOR_MSR'] = float(entry_MSR_VOOR.get())
                            user['parameters']['VOOR_VA'] = float(entry_VA_VOOR.get())
                            user['parameters']['VOOR_VPW'] = float(entry_VPW_VOOR.get())
                            user['parameters']['VOOR_AT'] = float(entry_AT_VOOR.get())
                            user['parameters']['VOOR_RT'] = float(entry_RT_VOOR.get())
                            user['parameters']['VOOR_RF'] = float(entry_RF_VOOR.get())
                            user['parameters']['VOOR_RTI'] = float(entry_RTI_VOOR.get())

                        elif label_state.cget("text") == "State: VVIR":
                            user['parameters']['VVIR_LRL'] = float(entry_LRL_VVIR.get())
                            user['parameters']['VVIR_URL'] = float(entry_URL_VVIR.get())
                            user['parameters']['VVIR_MSR'] = float(entry_MSR_VVIR.get())
                            user['parameters']['VVIR_VA'] = float(entry_VA_VVIR.get())
                            user['parameters']['VVIR_VPW'] = float(entry_VPW_VVIR.get())
                            user['parameters']['VVIR_VS'] = float(entry_VS_VVIR.get())
                            user['parameters']['VVIR_VRP'] = float(entry_VRP_VVIR.get())
                            user['parameters']['VVIR_AT'] = float(entry_AT_VVIR.get())
                            user['parameters']['VVIR_RT'] = float(entry_RT_VVIR.get())
                            user['parameters']['VVIR_RF'] = float(entry_RF_VVIR.get())
                            user['parameters']['VVIR_RTI'] = float(entry_RTI_VVIR.get())


            
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

        # 4 Buttons for AOOR,VOOR,AAIR,VVIR
        button_AOOR = tk.Button(main_window, text="AOOR", command=AOOR_pressed)
        button_AOOR.grid(row=3, column=0, sticky="n", padx=(130,65), pady=(30))  #Extra padding on its left side so its equal distance away from the edge
        button_VOOR = tk.Button(main_window, text="VOOR", command=VOOR_pressed)
        button_VOOR.grid(row=3, column=2, sticky="n", padx=65, pady=(30))
        button_AAIR = tk.Button(main_window, text="AAIR", command=AAIR_pressed)
        button_AAIR.grid(row=3, column=1, sticky="n", padx=65, pady=(30))
        button_VVIR = tk.Button(main_window, text="VVIR", command=VVIR_pressed)
        button_VVIR.grid(row=3, column=3, sticky="n", padx=65, pady=(30))
        

        button_save_state = tk.Button(main_window, text = "Save State", command=lambda : save_state(user_name))
        button_save_state.grid(row = 7, column = 5, sticky="s")

        #Displaying programmable parameters labels in left column
        label_lower_rate_limit = tk.Label(main_window, text="Lower Rate Limit (ppm) (30-175)")
        label_lower_rate_limit.grid(row=4, column=0, pady=(20,10), padx=(20,0), sticky="w")
        label_upper_rate_limit = tk.Label(main_window, text="Upper Rate Limit (ppm) (50-175)")
        label_upper_rate_limit.grid(row=5, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_amp = tk.Label(main_window, text="Atrial Amplitude (Volts) (0,0.5-3.2,3.5-7.0)")
        label_atrial_amp.grid(row=6, column=0, pady=10, padx=(20,0), sticky="w")
        label_atrial_pulse_width = tk.Label(main_window, text="Atrial Pulse Width (nanoseconds) (0.05, 0.1 - 1.9)")
        label_atrial_pulse_width.grid(row=7, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_amp = tk.Label(main_window, text="Ventricular Amplitude (Volts) (0,0.5-3.2,3.5-7.0)")
        label_ventricular_amp.grid(row=8, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_pulse_width = tk.Label(main_window, text="Ventricular Pulse Width (Nanoseconds) (0.05, 0.1 - 1.9)")
        label_ventricular_pulse_width.grid(row=9, column=0, pady=10, padx=(20,0), sticky="w")
        label_ventricular_sensitivity = tk.Label(main_window, text="Ventricular Sensitivity (milivolts) (0.25, 0.5, 0.75, 1.0 - 10)")
        label_ventricular_sensitivity.grid(row=10, column=0, pady=10, padx=(20,0), sticky="w")

        #Displaying programmable parameters labels in 2nd column
        label_atrial_sensitivity = tk.Label(main_window, text="Atrial Sensitivity (milivolts) (0.25, 0.5, 0.75, 1.0 - 10)")
        label_atrial_sensitivity.grid(row=4, column=2, pady=(20,10), padx=(20,0), sticky="w")
        label_ARP = tk.Label(main_window, text="ARP (miliseconds) (150 - 500)")
        label_ARP.grid(row=5, column=2, pady=10, padx=(20,0), sticky="w")
        label_VRP = tk.Label(main_window, text="VRP (miliseconds) (150 - 500)")
        label_VRP.grid(row=6, column=2, pady=10, padx=(20,0), sticky="w")
        label_PVARP = tk.Label(main_window, text="PVARP (miliseconds) (150 - 500)")
        label_PVARP.grid(row=7, column=2, pady=10, padx=(20,0), sticky="w")
        label_hysteresis = tk.Label(main_window, text="Hysteresis (ppm) (Off or 30-175)")
        label_hysteresis.grid(row=8, column=2, pady=10, padx=(20,0), sticky="w")
        label_rate_smoothing = tk.Label(main_window, text="Rate Smoothing (%) (Off, 3, 6, 9, 12, 15, 18, 21, 25)")
        label_rate_smoothing.grid(row=9, column=2, pady=10, padx=(20,0), sticky="w")

        label_maximum_sensor_rate = tk.Label(main_window, text="maximum sensor rate (ppm) (30-175)")
        label_maximum_sensor_rate.grid(row=10, column=2, pady=10, padx=(20,0), sticky="w")

        label_activity_threshold = tk.Label(main_window, text="activity threshold V-Low, Low, Med-Low, Med, Med-High, High, V-High")
        label_activity_threshold.grid(row=11, column=0, pady=10, padx=(20,0), sticky="w")

        label_reaction_time = tk.Label(main_window, text="reaction time (seconds) (10-50)")
        label_reaction_time.grid(row=12, column=0, pady=10, padx=(20,0), sticky="w")

        label_response_factor = tk.Label(main_window, text="response factor (1-16)")
        label_response_factor.grid(row=11, column=2, pady=10, padx=(20,0), sticky="w")

        label_recovery_time = tk.Label(main_window, text="recovery time (min) (2-16)")
        label_recovery_time.grid(row=12, column=2, pady=10, padx=(20,0), sticky="w")



