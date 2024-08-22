import json
import tkinter as tk
from tkinter import ttk
import random

# Define the Character class
class Character:
    def __init__(self, id, src, name, skills, inventory, type):
        self.id = id
        self.src = src
        self.name = name
        self.skills = skills
        self.inventory = inventory
        self.type = type

# Define the Skill class
class Skill:
    def __init__(self, id, title, level, experience):
        self.id = id
        self.title = title
        self.level = level
        self.experience = experience

    def add_experience(self, amount):
        self.experience += amount
        # Level up logic (simplified)
        if self.experience >= self.level * 100:
            self.level += 1
            self.experience = 0

# Define the Inventory class
class Inventory:
    def __init__(self, currency, woodcutting_resources):
        self.currency = currency
        self.woodcutting_resources = woodcutting_resources

    def add_logs(self, log_type, amount):
        if log_type in self.woodcutting_resources:
            self.woodcutting_resources[log_type] += amount

# Define the WoodcuttingData class
class WoodcuttingData:
    def __init__(self, id, title, type, level_range, experience_range, axes, trees, resources, gui):
        self.id = id
        self.title = title
        self.type = type
        self.level_range = level_range
        self.experience_range = experience_range
        self.axes = axes
        self.trees = trees
        self.resources = resources
        self.gui = gui

# Load the JSON data
character_json = '''{
  "character": {
    "id": 0,
    "src": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/blondeBear/blondeBear.webp",
    "name": "Mosberg",
    "skills": [
      {
        "id": 0,
        "title": "Woodcutting",
        "level": 1,
        "experience": 0
      }
    ],
    "inventory": {
      "currency": {
        "gold": 0
      },
      "woodcuttingResources": {
        "logs": 0,
        "oak_logs": 0,
        "willow_logs": 0,
        "maple_logs": 0,
        "yew_logs": 0,
        "magic_logs": 0
      }
    },
    "type": "Player"
  }
}'''

woodcutting_data_json = '''{
  "woodcuttingData": {
    "id": 0,
    "title": "Woodcutting",
    "type": "Gathering",
    "levelRange": {
      "min": 1,
      "max": 99
    },
    "experienceRange": {
      "min": 0,
      "max": 13034431
    },
    "axes": [
      {
        "id": 1,
        "level": 1,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/tools/axes/bronze_axe.webp",
        "alt": "Bronze Axe Tool",
        "logChance": 0.75,
        "description": "A sturdy bronze axe for chopping logs.",
        "marketPrices": {
          "buy": 10,
          "sell": 5
        }
      },
      {
        "id": 2,
        "level": 1,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/tools/axes/iron_axe.webp",
        "alt": "Iron Axe Tool",
        "logChance": 1.5,
        "description": "A robust iron axe for efficient log chopping.",
        "marketPrices": {
          "buy": 20,
          "sell": 10
        }
      }
    ],
    "trees": [
      {
        "id": 9,
        "level": 1,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/objects/trees/tree.webp",
        "alt": "Tree Object",
        "resourceId": 15,
        "timers": [
          {
            "type": "despawn",
            "duration": 16.6
          },
          {
            "type": "respawn",
            "duration": 5.4
          }
        ],
        "logChance": 1.0,
        "description": "A common tree found in the forest."
      },
      {
        "id": 10,
        "level": 15,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/objects/trees/oak_tree.webp",
        "alt": "Oak Tree Object",
        "resourceId": 16,
        "timers": [
          {
            "type": "despawn",
            "duration": 27
          },
          {
            "type": "respawn",
            "duration": 8.4
          }
        ],
        "logChance": 0.8,
        "description": "A sturdy oak tree with valuable logs."
      }
    ],
    "resources": [
      {
        "id": 15,
        "level": 1,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/resources/logs/logs.webp",
        "alt": "Logs Resource",
        "experience": 25,
        "description": "Common logs used for crafting and fuel.",
        "marketPrices": {
          "buy": 10,
          "sell": 5
        }
      },
      {
        "id": 16,
        "level": 15,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/resources/logs/oak_logs.webp",
        "alt": "Oak Logs Resource",
        "experience": 37.5,
        "description": "Valuable oak logs used for advanced crafting.",
        "marketPrices": {
          "buy": 20,
          "sell": 10
        }
      }
    ],
    "gui": [
      {
        "id": 21,
        "imageName": "https://raw.githubusercontent.com/Mosberg/assets/main/images/WEBP/game/gui/tabs/inventory_tab.webp",
        "alt": "Inventory GUI"
      }
    ]
  }
}'''

# Parse the JSON data
character_data = json.loads(character_json)
woodcutting_data = json.loads(woodcutting_data_json)

# Create instances of the classes
character = Character(
    id=character_data['character']['id'],
    src=character_data['character']['src'],
    name=character_data['character']['name'],
    skills=[Skill(**skill) for skill in character_data['character']['skills']],
    inventory=Inventory(
        currency=character_data['character']['inventory']['currency'],
        woodcutting_resources=character_data['character']['inventory']['woodcuttingResources']
    ),
    type=character_data['character']['type']
)

woodcutting = WoodcuttingData(
    id=woodcutting_data['woodcuttingData']['id'],
    title=woodcutting_data['woodcuttingData']['title'],
    type=woodcutting_data['woodcuttingData']['type'],
    level_range=woodcutting_data['woodcuttingData']['levelRange'],
    experience_range=woodcutting_data['woodcuttingData']['experienceRange'],
    axes=woodcutting_data['woodcuttingData']['axes'],
    trees=woodcutting_data['woodcuttingData']['trees'],
    resources=woodcutting_data['woodcuttingData']['resources'],
    gui=woodcutting_data['woodcuttingData']['gui']
)

# Create the main application window
root = tk.Tk()
root.title("Idle Game")

# Create a frame for the character information
character_frame = ttk.LabelFrame(root, text="Character")
character_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Display character name
ttk.Label(character_frame, text=f"Name: {character.name}").grid(row=0, column=0, padx=5, pady=5)

# Display character skill level
ttk.Label(character_frame, text=f"Woodcutting Level: {character.skills[0].level}").grid(row=1, column=0, padx=5, pady=5)

# Display character gold
ttk.Label(character_frame, text=f"Gold: {character.inventory.currency['gold']}").grid(row=2, column=0, padx=5, pady=5)

# Create a frame for the woodcutting information
woodcutting_frame = ttk.LabelFrame(root, text="Woodcutting")
woodcutting_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Display woodcutting axes
ttk.Label(woodcutting_frame, text="Axes:").grid(row=0, column=0, padx=5, pady=5)
for i, axe in enumerate(woodcutting.axes):
    ttk.Label(woodcutting_frame, text=f"{axe['description']} (Level {axe['level']})").grid(row=i+1, column=0, padx=5, pady=5)

# Display woodcutting trees
ttk.Label(woodcutting_frame, text="Trees:").grid(row=0, column=1, padx=5, pady=5)
for i, tree in enumerate(woodcutting.trees):
    ttk.Label(woodcutting_frame, text=f"{tree['description']} (Level {tree['level']})").grid(row=i+1, column=1, padx=5, pady=5)

# Display woodcutting resources
ttk.Label(woodcutting_frame, text="Resources:").grid(row=0, column=2, padx=5, pady=5)
for i, resource in enumerate(woodcutting.resources):
    ttk.Label(woodcutting_frame, text=f"{resource['description']} (Level {resource['level']})").grid(row=i+1, column=2, padx=5, pady=5)

# Function to chop a tree
def chop_tree(tree, axe):
    if character.skills[0].level >= tree['level']:
        if random.random() < axe['logChance']:
            log_type = 'logs' if tree['resourceId'] == 15 else 'oak_logs'
            character.inventory.add_logs(log_type, 1)
            character.skills[0].add_experience(woodcutting.resources[tree['resourceId'] - 15]['experience'])
            update_inventory()
            update_skill()

# Function to update the inventory display
def update_inventory():
    logs_label.config(text=f"Logs: {character.inventory.woodcutting_resources['logs']}")
    oak_logs_label.config(text=f"Oak Logs: {character.inventory.woodcutting_resources['oak_logs']}")

# Function to update the skill display
def update_skill():
    skill_label.config(text=f"Woodcutting Level: {character.skills[0].level} (XP: {character.skills[0].experience})")

# Create buttons for chopping trees
for i, tree in enumerate(woodcutting.trees):
    ttk.Button(woodcutting_frame, text=f"Chop {tree['description']}", command=lambda t=tree: chop_tree(t, woodcutting.axes[0])).grid(row=i+1, column=3, padx=5, pady=5)

# Display inventory
inventory_frame = ttk.LabelFrame(root, text="Inventory")
inventory_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

logs_label = ttk.Label(inventory_frame, text=f"Logs: {character.inventory.woodcutting_resources['logs']}")
logs_label.grid(row=0, column=0, padx=5, pady=5)

oak_logs_label = ttk.Label(inventory_frame, text=f"Oak Logs: {character.inventory.woodcutting_resources['oak_logs']}")
oak_logs_label.grid(row=1, column=0, padx=5, pady=5)

# Display skill
skill_label = ttk.Label(character_frame, text=f"Woodcutting Level: {character.skills[0].level} (XP: {character.skills[0].experience})")
skill_label.grid(row=1, column=0, padx=5, pady=5)

# Run the application
root.mainloop()
