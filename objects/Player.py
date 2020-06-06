import numpy as np
from data.database import step_by_command
import random


class Player():
    def __init__(self, location, inventory, health):
        self.inventory = inventory
        self.coordinate_location = location
        self.health = health

    def random_random_step(self):
        step_command = random.choice(list(step_by_command.keys()))
        return step_command

    def change_sate_by_step(self, command):
        self.coordinate_location += step_by_command[command]

    def change_location_by_teleport(self, coordinates_holes):
        current_hole_ind = [list(i) for i in coordinates_holes].index(list(self.coordinate_location))
        number_holes = len(coordinates_holes)
        next_hole_coordinate = (current_hole_ind + 1) % number_holes
        self.coordinate_location = np.array((coordinates_holes[next_hole_coordinate]))

    def add_treasure(self):
        self.inventory.append('treasure')

    def get_state(self):
        return {'coordinate_location':self.coordinate_location, 'inventory':self.inventory}
    
    def change_coordinate_river(self, river_coordinates):
        current_river_index = [list(i) for i in river_coordinates].index(list(self.coordinate_location))
        lenght_river = len(river_coordinates)
        next_rivercell_index = current_river_index + 2
        if next_rivercell_index >= lenght_river:
            next_rivercell_index = lenght_river - 1
        self.coordinate_location = np.array((river_coordinates[next_rivercell_index]))

