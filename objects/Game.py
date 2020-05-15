
from  objects.Player import Player
from  objects.Labyrinth import Labyrinth
from objects.Checker import Checker
from data.database import *

class Game():
    def __init__(self, config):
        self.game_lab = Labyrinth(config['size'], config['objects'])
        self.game_lab.generate_wals()
        self.game_lab.generate_exit()
        self.game_lab.generate_treasure_coordinate()
        self.game_lab.generate_warmHoles(config['num_holes'])
        self.player = Player(self.game_lab.exit_doorstep_coord, config['inventory'])
        self.game_end = False
        self.checker = Checker(self.game_lab)
    
    def step(self, command):
        command_possible, command_respond = self.checker.check_command(command, self.player)
        print(command_respond)
        if command_respond == 'step executed, treasure':
            self.player.add_treasure()
            # self.labyrinth.delete_theasure
        if command_possible:
            if command == 'keep':
                coordinate_holes = self.game_lab.dict_object['holes'].list_coordinates
                if tuple(self.player.coordinate_location) in coordinate_holes:
                    print('teleport')
                    self.player.change_state_by_teleport(coordinate_holes)
            else:
                self.player.change_sate_by_step(command)
        if command_respond == 'step executed, open exit':
            self.game_end = True

    def show_map(self):
        print(self.game_lab.map_labyrinth)


if __name__ == '__main__':
    test_config = {'size':4, 'num_holes':3, 'inventory':[], 'objects':{}}
    test_game = Game(test_config)
    print(test_game.game_lab.map_labyrinth)
    command = ''
    while command != 'stop':
        command = input ()
        if command == 'h':
            print(test_game.player.coordinate_location, test_game.player.inventory)
        else:
            test_game.step(command)

