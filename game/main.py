# main.py
import tkinter as tk
from tkinter import ttk
from character import Character
from woodcutting import WoodcuttingData
from gui import create_gui
import json

# Load the character data
with open('/data/character.json') as f:
    character_data = Character(**json.load(f))

# Load the woodcutting data
with open('/data/woodcutting.json') as f:
    woodcutting_data = WoodcuttingData(**json.load(f))

# Create the main application window
root = tk.Tk()
root.title("Idle Game")

# Create the GUI components
create_gui(root, character_data, woodcutting_data)

# Run the application
root.mainloop()