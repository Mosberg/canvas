# gui.py
import tkinter as tk
from tkinter import ttk

def create_gui(root, character_data, woodcutting_data):
    # Create the character frame
    character_frame = ttk.LabelFrame(root, text="Character")
    character_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Create the woodcutting frame
    woodcutting_frame = ttk.LabelFrame(root, text="Woodcutting")
    woodcutting_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Create the inventory frame
    inventory_frame = ttk.LabelFrame(root, text="Inventory")
    inventory_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # Create the GUI components
    create_character_gui(character_frame, character_data)
    create_woodcutting_gui(woodcutting_frame, woodcutting_data)
    create_inventory_gui(inventory_frame, character_data)

def create_character_gui(frame, character_data):
    # Create the character name label
    ttk.Label(frame, text=f"Name: {character_data.name}").grid(row=0, column=0, padx=5, pady=5)

    # Create the character skill level label
    ttk.Label(frame, text=f"Woodcutting Level: {character_data.skills[0]['level']}").grid(row=1, column=0, padx=5, pady=5)

    # Create the character inventory label
    ttk.Label(frame, text=f"Inventory: {character_data.inventory}").grid(row=2, column=0, padx=5, pady=5)

    # Create the character type label
    ttk.Label(frame, text=f"Type: {character_data.type}").grid(row=3, column=0, padx=5, pady=5)

    # Create the character image
    character_image = tk.PhotoImage(file=character_data.src)
    ttk.Label(frame, image=character_image).grid(row=4, column=0, padx=5, pady=5)
    
    # Create the character ID label
    ttk.Label(frame, text=f"ID: {character_data.id}").grid(row=5, column=0, padx=5, pady=5)

def create_woodcutting_gui(frame, woodcutting_data):
    # Create the woodcutting axes label
    ttk.Label(frame, text="Axes:").grid(row=0, column=0, padx=5, pady=5)
    for i, axe in enumerate(woodcutting_data.axes):
        ttk.Label(frame, text=f"{axe['description']} (Level {axe['level']})").grid(row=i+1, column=0, padx=5, pady=5)

    # Create the woodcutting trees label
    ttk.Label(frame, text="Trees:").grid(row=0, column=1, padx=5, pady=5)
    for i, tree in enumerate(woodcutting_data.trees):
        ttk.Label(frame, text=f"{tree['description']} (Level {tree['level']})").grid(row=i+1, column=1, padx=5, pady=5)

    # Create the woodcutting resources label
    ttk.Label(frame, text="Resources:").grid(row=0, column=2, padx=5, pady=5)
    for i, resource in enumerate(woodcutting_data.resources):
        ttk.Label(frame, text=f"{resource['description']} (Level {resource['level']})").grid(row=i+1, column=2, padx=5, pady=5)

def create_inventory_gui(frame, character_data):
    # Create the logs label
    ttk.Label(frame, text=f"Logs: {character_data.inventory['woodcutting_resources']['logs']}").grid(row=0, column=0, padx=5, pady=5)

    # Create the oak logs label
    ttk.Label(frame, text=f"Oak Logs: {character_data.inventory['woodcutting_resources']['oak_logs']}").grid(row=1, column=0, padx=5, pady=5)