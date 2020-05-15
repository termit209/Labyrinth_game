
import numpy as np
from data.database import * 

#dict_icon_labyrinth_object = {'wall':'W',
#                              'monolith':'M',
#                              'treasure':'T',
#                              'hole':'H',
#                              'exit':'E'}

#step_by_command = {'go up':np.array((-2, 0)), 'go down':np.array((2, 0)), 
#                       'go left':np.array((0, -2)), 'go right':np.array((0, 2)), 'keep':np.array((0, 0))}

class Checker():
    def __init__(self, labyrinth):
        self.map_labyrinth = labyrinth.map_labyrinth
        self.dict_lab_object = labyrinth.dict_object

    def crossing_wall_by_command(self, command, player):
        command_step = step_by_command[command]
        current_location = player.coordinate_location
        crossing_cell_X = int(current_location[0] + (command_step[0]/2))
        crossing_cell_Y = int(current_location[1] + (command_step[1]/2))
        return (crossing_cell_X, crossing_cell_Y)

    def cell_after_command(self, command, player):
        command_step = step_by_command[command]
        current_location = player.coordinate_location
        cell_X = int(current_location[0] + command_step[0])
        cell_Y = int(current_location[1] + command_step[1])
        return (cell_X, cell_Y)

    def is_wall_towards(self, command, player):
        cell_crossing_wall = self.crossing_wall_by_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['wall']

    def is_monolith_towards(self, command, player):
        cell_crossing_wall = self.crossing_wall_by_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['monolith']

    def is_exit_towards(self, command, player):
        cell_crossing_wall = self.crossing_wall_by_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['exit']

    def is_command_possible(self, command, player):
        is_possibility = self.is_monolith_towards(command, player)
        is_possibility |= self.is_wall_towards(command, player)
        is_treasure_have = 'treasure' in player.inventory
        is_possibility |= (self.is_exit_towards(command, player) and is_treasure_have)
        return is_possibility
    
    def is_treasure_towards(self, command, player):
        cell_crossing_wall = self.cell_after_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['treasure']

    def is_holes_towards(self, command, player):
        cell_crossing_wall = self.cell_after_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['hole']

    def is_river_towards(self, command, player):
        cell_crossing_wall = self.cell_after_command(command, player)
        return self.map_labyrinth[cell_crossing_wall[0]][cell_crossing_wall[1]] == dict_icon_labyrinth_object['river']
    
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
        return (True, 'step executed')


if __name__ == '__main__':
    from Player import Player
    from Labyrinth import Labyrinth
    test_player = Player(np.array((1, 1)), [])
    test_lab = Labyrinth(4, {})
    test_lab.generate_wals()
    test_lab.generate_exit()
    test_lab.generate_treasure_coordinate()
    test_lab.generate_warmHoles(2)
    test_checker = Checker(test_lab)
    print(test_lab.map_labyrinth)
    print((np.array(test_lab.dict_object['treasure'].coordinate) - np.array((0, 2))))

    test2_player = Player(np.array(test_lab.dict_object['treasure'].coordinate) - np.array((0, 2)), [])
    print(test2_player.coordinate_location)
    for command in  step_by_command.keys():
        print(command, test_checker.check_command(command, test2_player))
