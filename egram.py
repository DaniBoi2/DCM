import tkinter as tk
from tkinter import *
import json
import os
import copy

from struct import pack 

class Egram:
    def __init__(self, filename, x_offset, y_offset):
        self.filename = filename
        self.x_offset = x_offset
        self.y_offset = y_offset

        # Define the serial port settings
        self.serial_port = "COM4"  # Change this to your specific serial port
        self.baud_rate = 115200  # Change this to your specific baud rate

        # current mode data
        self.cur_mode = { "state": 1, "AA": 0,
    "APW": 0,
    "ARP": 0,
    "AS": 0,
    "ATD": 0,
    "VA": 0,
    "VPW": 0,
    "VRP": 0,
    "VS": 0,
    "VTD": 0,
    "LRL": 0,
    "URL": 0,
    "MSR": 0,
    "AVD": 0,
    "PVARP": 0,
    "AT": 0,
    "RT": 0,
    "RF": 0,
    "RTI": 0}
        
        

    def egram_screen(self):
         # Create the window, labels, entry widgets, button, etc.
        egram_window = tk.Tk()
        egram_window.title("Login")
        egram_window.geometry(f"700x400+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        egram_window.resizable(False, False)
        top_label = tk.Label(egram_window, text="Egram Data for : ", )
        top_label.pack()



    def transmit_data(self, user, state):
        
        
        # Convert the parameters to a JSON string
        all_modes_data = user["parameters"]
        
        one_mode_data = {}

        if state == "AOO":
            self.cur_mode["AA"] = all_modes_data["AOO_AA"]
            self.cur_mode["APW"] = all_modes_data["AOO_APW"]
            self.cur_mode["LRL"] = all_modes_data["AOO_LRL"]
            self.cur_mode["URL"] = all_modes_data["AOO_URL"]

            
        elif state == "AAI":
            self.cur_mode["state"] = 2
            self.cur_mode["AA"] = all_modes_data["AAI_AA"]
            self.cur_mode["APW"] = all_modes_data["AAI_APW"]
            self.cur_mode["LRL"] = all_modes_data["AAI_LRL"]
            self.cur_mode["URL"] = all_modes_data["AAI_URL"]
            self.cur_mode["AS"] = all_modes_data["AAI_AS"]
            self.cur_mode["ARP"] = all_modes_data["AAI_ARP"]
            self.cur_mode["PVARP"] = all_modes_data["AAI_PVARP"]
        elif state == "VOO": 
            self.cur_mode["state"] = 3
            self.cur_mode["AA"] = all_modes_data["VOO_AA"]
            self.cur_mode["APW"] = all_modes_data["VOO_APW"]
            self.cur_mode["LRL"] = all_modes_data["VOO_LRL"]
            self.cur_mode["URL"] = all_modes_data["VOO_URL"]
        elif state == "VVI":
            self.cur_mode["state"] = 4
            self.cur_mode["VA"] = all_modes_data["VVI_VA"]
            self.cur_mode["VPW"] = all_modes_data["VVI_VPW"]
            self.cur_mode["VS"] = all_modes_data["VVI_VS"]
            self.cur_mode["VRP"] = all_modes_data["VVI_VRP"]
            self.cur_mode["LRL"] = all_modes_data["VVI_LRL"]
            self.cur_mode["URL"] = all_modes_data["VVI_URL"]
        elif state == "AOOR": 
            self.cur_mode["state"] = 5
            self.cur_mode["LRL"] = all_modes_data["AOOR_LRL"]
            self.cur_mode["URL"] = all_modes_data["AOOR_URL"]
            self.cur_mode["MSR"] = all_modes_data["AOOR_MSR"]
            self.cur_mode["AA"] = all_modes_data["AOOR_AA"]
            self.cur_mode["APW"] = all_modes_data["AOOR_APW"]
            self.cur_mode["AT"] = all_modes_data["AOOR_AT"]
            self.cur_mode["RT"] = all_modes_data["AOOR_RT"]
            self.cur_mode["RF"] = all_modes_data["AOOR_RF"]
            self.cur_mode["RTI"] = all_modes_data["AOOR_RTI"]
        elif state == "AAIR":
            self.cur_mode["state"] = 6
            self.cur_mode["LRL"] = all_modes_data["AAIR_LRL"]
            self.cur_mode["URL"] = all_modes_data["AAIR_URL"]
            self.cur_mode["MSR"] = all_modes_data["AAIR_MSR"]
            self.cur_mode["AA"] = all_modes_data["AAIR_AA"]
            self.cur_mode["APW"] = all_modes_data["AAIR_APW"]

            self.cur_mode["AS"] = all_modes_data["AAIR_AS"]
            self.cur_mode["ARP"] = all_modes_data["AAIR_ARP"]
            self.cur_mode["PVARP"] = all_modes_data["AAIR_AS"]

            self.cur_mode["AT"] = all_modes_data["AAIR_AT"]
            self.cur_mode["RT"] = all_modes_data["AAIR_RT"]
            self.cur_mode["RF"] = all_modes_data["AAIR_RF"]
            self.cur_mode["RTI"] = all_modes_data["AAIR_RTI"]

        elif state == "VOOR":

            self.cur_mode["state"] = 7
            self.cur_mode["LRL"] = all_modes_data["VOOR_LRL"]
            self.cur_mode["URL"] = all_modes_data["VOOR_URL"]
            self.cur_mode["MSR"] = all_modes_data["VOOR_MSR"]
            self.cur_mode["VA"] = all_modes_data["VOOR_VA"]
            self.cur_mode["VPW"] = all_modes_data["VOOR_VPW"]

            self.cur_mode["AT"] = all_modes_data["VOOR_AT"]
            self.cur_mode["RT"] = all_modes_data["VOOR_RT"]
            self.cur_mode["RF"] = all_modes_data["VOOR_RF"]
            self.cur_mode["RTI"] = all_modes_data["VOOR_RTI"]

           
        elif state == "VVIR": 


            self.cur_mode["LRL"] = all_modes_data["VVIR_LRL"]
            self.cur_mode["URL"] = all_modes_data["VVIR_URL"]
            self.cur_mode["MSR"] = all_modes_data["VVIR_MSR"]
            self.cur_mode["VA"] = all_modes_data["VVIR_VA"]
            self.cur_mode["VPW"] = all_modes_data["VVIR_VPW"]
            self.cur_mode["VS"] = all_modes_data["VVIR_VS"]
            self.cur_mode["VRP"] = all_modes_data["VVIR_VRP"]

            self.cur_mode["AT"] = all_modes_data["VVIR_AT"]
            self.cur_mode["RT"] = all_modes_data["VVIR_RT"]
            self.cur_mode["RF"] = all_modes_data["VVIR_RF"]
            self.cur_mode["RTI"] = all_modes_data["VVIR_RTI"]
        else: 
            # debug here properly
            print("state not selected")

        print(state)

        # double d, uint16 H, 
        output_data = pack("<HdHHdddHHddhhhhhdhhh", 16, 55, 
        self.cur_mode["state"], 
        self.cur_mode["AA"], 
        self.cur_mode["APW"], 
        self.cur_mode["ARP"], 
        self.cur_mode["AS"], 
        self.cur_mode["ATD"], 
        self.cur_mode["VA"], 
        self.cur_mode["VPW"],
        self.cur_mode["VRP"], 
        self.cur_mode["VS"], 
        self.cur_mode["VTD"], 
        self.cur_mode["LRL"], 
        self.cur_mode["URL"], 
        self.cur_mode["MSR"], 
        self.cur_mode["AVD"], 
        self.cur_mode["PVARP"], 
        self.cur_mode["AT"], 
        self.cur_mode["RT"], 
        self.cur_mode["RF"], 
        self.cur_mode["RTI"])


        # Open the serial port
        ser = serial.Serial(self.serial_port, self.baud_rate)

        # send data via UART
        ser.write(output_data)

        # Close the serial port
        ser.close()

        