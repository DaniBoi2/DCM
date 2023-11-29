import tkinter as tk
from tkinter import *
import json
import os

class Egram:
    def __init__(self, filename, x_offset, y_offset):
        self.filename = filename
        self.x_offset = x_offset
        self.y_offset = y_offset
        

    def egram_screen(self):
         # Create the window, labels, entry widgets, button, etc.
        egram_window = tk.Tk()
        egram_window.title("Login")
        egram_window.geometry(f"700x400+{self.x_offset}+{self.y_offset}")  #Displaying it roughly in the center of the user screen
        egram_window.resizable(False, False)
        top_label = tk.Label(egram_window, text="Egram Data for : ", )
        top_label.pack()