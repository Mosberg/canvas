# character.py
import json

class Character:
    def __init__(self, id, src, name, skills, inventory, type):
        self.id = id
        self.src = src
        self.name = name
        self.skills = skills
        self.inventory = inventory
        self.type = type