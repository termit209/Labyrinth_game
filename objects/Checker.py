
import numpy as np
from data.database import * 
from objects.Player import Player
from objects.Labyrinth import Labyrinth


class Checker():
    def __init__(self, labyrinth):
        self.map_labyrinth = labyrinth.map_labyrinth
        self.dict_lab_object = labyrinth.dict_object

    def cell_after_command(self, command, player):
        command_step = step_by_command[command]
        current_location = player.coordinate_location
        return current_location + command_step

    def is_wall_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['wall']

    def is_monolith_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['monolith']

    def is_exit_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['exit']

    def is_command_possible(self, command, player):
        is_possibility = self.is_monolith_towards(command, player)
        is_possibility |= self.is_wall_towards(command, player)
        is_treasure_have = 'treasure' in player.inventory
        is_possibility |= (self.is_exit_towards(command, player) and is_treasure_have)
        return is_possibility
    
    def is_treasure_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['treasure']

    def is_holes_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['hole']

    def is_river_towards(self, command, player):
        new_cell = self.cell_after_command(command, player)
        return self.map_labyrinth[new_cell[0], new_cell[1]] == dict_icon_labyrinth_object['river']
    
    def check_command(self, command, player):
        if self.is_monolith_towards(command, player):
           return (False, 'step impossible, monolith')
        if self.is_wall_towards(command, player):
            return (False, 'step impossible, wall')
        if self.is_exit_towards(command, player):
            is_treasure_have = 'treasure' in player.inventory
            if is_treasure_have:
                return (True, 'step executed, open exit')
            else:
                return (False, 'step impossible, close exit')
        if self.is_treasure_towards(command, player):
            return (True, 'step executed, treasure')
        if self.is_holes_towards(command, player):
            return (True, 'step executed, hole')
        if self.is_river_towards(command, player):
            return (True, 'step executed, river')
        return (True, 'step executed')

