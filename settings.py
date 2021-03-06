#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:03:39 2020

@author: zunus
"""

import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        settings_container = ttk.Frame(self, padding = "30 15 30 15")
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)
        
        pomodoro_label = ttk.Label(settings_container, text="Pomodoro : ")
        pomodoro_label.grid(row=0, column=0, sticky="W")
        
        pomodoro_input = tk.Spinbox(settings_container, from_=0, to=120, increment=1, justify="center", textvariable=controller.pomodoro, width=10)
        pomodoro_input.grid(row=0, column=1, sticky="EW")
        pomodoro_input.focus()
        
        
        long_break_label = ttk.Label(settings_container, text="Long break time : ")
        long_break_label.grid(row=1, column=0, sticky="W")
        long_break_input = tk.Spinbox(settings_container, from_=0, to=115, increment=1, justify="center", textvariable=controller.long_break, width=10)
        long_break_input.grid(row=1, column=1, sticky="EW")
        
        short_break_label = ttk.Label(settings_container, text="Short break time : ")
        short_break_label.grid(row=2, column=0, sticky="W")
        short_break_input = tk.Spinbox(settings_container, from_=0, to=100, increment=1, justify="center", textvariable=controller.short_break, width=10)
        short_break_input.grid(row=2, column=1, sticky="EW")

        
        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)
            