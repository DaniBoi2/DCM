import tkinter as tk
from tkinter import *
import json
import os
import copy

from struct import pack 
import serial
import matplotlib.pyplot as plt
import numpy as np

class Uart:
    def __init__(self, filename, x_offset, y_offset):
        self.filename = filename
        self.x_offset = x_offset
        self.y_offset = y_offset

        # Define the serial port settings
        self.serial_port = "COM3"  # Change this to your specific serial port
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
        top_label = tk.Label(egram_window, text="Egram Plots", font=("Arial", 16))
        top_label.grid(row=0, column=0, columnspan=3, sticky="n", padx=(20), pady=(10, 50))

        button_vent = tk.Button(egram_window, text="ventricle", command=lambda : self.plot_vent())
        button_vent.grid(row=1, column=0, sticky="w", padx=70)  

        button_atri = tk.Button(egram_window, text="atrium", command=lambda : self.plot_atri())
        button_atri.grid(row=1, column=1, sticky="nsew", padx=70)  # Set sticky="nsew" to make the button expand in all directions (center)

        button_both = tk.Button(egram_window, text="both", command=lambda : self.plot_both())
        button_both.grid(row=1, column=2, sticky="e", padx=70,)  # Set sticky="e" to align the button to the east (right)

        # Adjusting the layout
        # egram_window.grid_columnconfigure(1, weight=1) 

    def plot_vent(self):
                
        x = np.linspace(0, 10, 100)
        y = np.zeros(100)

        # Create the plot
        plt.plot(x, y, label='ventricle plot')
        plt.title('Venctricle')
        plt.xlabel('time')
        plt.ylabel('signal')
        plt.legend()
        plt.grid(True)

        # Show the plot
        plt.show()

    def plot_atri(self):
                
        x = np.linspace(0, 10, 100)
        y = np.zeros(100)

        # Create the plot
        plt.plot(x, y, label='atrium plot')
        plt.title('atrium')
        plt.xlabel('time')
        plt.ylabel('signal')
        plt.legend()
        plt.grid(True)

        # Show the plot
        plt.show()

    def plot_both(self): 
    
        # Create the x values
        x = np.linspace(0, 10, 100)

        # Create the first set of y values (all zeros)
        y1 = np.zeros(100)

        # Create the second set of y values (a simple linear function as an example)
        y2 = np.zeros(100)

        # Create the plot
        plt.plot(x, y1, label='Plot 1 ventricular')
        plt.plot(x, y2, label='Plot 2 atrium')
        
        plt.title('Ventricle and Atrium')
        plt.xlabel('time')
        plt.ylabel('signal')
        plt.legend()
        plt.grid(True)

        # Show the plot
        plt.show()

    def transmit_data(self, user, state):
        
        
        # Convert the parameters to a JSON string
        all_modes_data = user["parameters"]
        
        one_mode_data = {}

        if state == "AOO":
            self.cur_mode["state"] = 1
            self.cur_mode["AA"] = all_modes_data["AOO_AA"]
            self.cur_mode["APW"] = all_modes_data["AOO_APW"]
            self.cur_mode["LRL"] = all_modes_data["AOO_LRL"]
            self.cur_mode["URL"] = all_modes_data["AOO_URL"]

            
        elif state == "AAI":
            self.cur_mode["state"] = 3
            self.cur_mode["AA"] = all_modes_data["AAI_AA"]
            self.cur_mode["APW"] = all_modes_data["AAI_APW"]
            self.cur_mode["LRL"] = all_modes_data["AAI_LRL"]
            self.cur_mode["URL"] = all_modes_data["AAI_URL"]
            self.cur_mode["AS"] = all_modes_data["AAI_AS"]
            self.cur_mode["ARP"] = all_modes_data["AAI_ARP"]
            self.cur_mode["PVARP"] = all_modes_data["AAI_PVARP"]
        elif state == "VOO": 
            self.cur_mode["state"] = 2
            self.cur_mode["AA"] = all_modes_data["VOO_VA"]
            self.cur_mode["APW"] = all_modes_data["VOO_VPW"]
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
            self.cur_mode["state"] = 7
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

            self.cur_mode["state"] = 6
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

            self.cur_mode["state"] = 8
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
        output_data = pack("<BBBdHHdddHHddHHHHHdHHH", 
        16, 
        20, 
        int(self.cur_mode["state"]), 
        int(self.cur_mode["AA"]), 
        int(self.cur_mode["APW"]), 
        int(self.cur_mode["ARP"]), 
        int(self.cur_mode["AS"]), 
        int(self.cur_mode["ATD"]), 
        int(self.cur_mode["VA"]),
        int(self.cur_mode["VPW"]),
        int(self.cur_mode["VRP"]), 
        int(self.cur_mode["VS"]),
        int(self.cur_mode["VTD"]), 
        int(self.cur_mode["LRL"]), 
        int(self.cur_mode["URL"]), 
        int(self.cur_mode["MSR"]), 
        int(self.cur_mode["AVD"]), 
        int(self.cur_mode["PVARP"]), 
        int(self.cur_mode["AT"]), 
        int(self.cur_mode["RT"]), 
        int(self.cur_mode["RF"]), 
        int(self.cur_mode["RTI"])
        )


        # Open the serial port
        ser = serial.Serial(self.serial_port, self.baud_rate)

        # send data via UART
        ser.write(output_data)
        print(output_data)

        # Close the serial port
        ser.close()

        