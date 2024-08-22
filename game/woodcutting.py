# woodcutting.py
import json

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