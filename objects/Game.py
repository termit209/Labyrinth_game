import random
import numpy as numpy

from  objects.Player import Player
from  objects.Labyrinth import Labyrinth
from objects.Checker import Checker
from data.database import *

class Game():
    def __init__(self, config):
        self.config = config
        self.game_end = False

    def create_labyrinth(self):
        self.game_labyrinth = Labyrinth(self.config['size'], {})
        self.game_labyrinth.generate_monoliths()
        self.game_labyrinth.generate_walls()
        self.game_labyrinth.generate_exit()
        self.game_labyrinth.generate_treasure()
        if self.config['num_holes'] > 0:
            self.game_labyrinth.generate_warmholes(self.config['num_holes'])
        if self.config['lenght_river'] > 0:
            self.game_labyrinth.generate_river(self.config['lenght_river'])

    def create_cheker(self):
        self.checker = Checker(self.game_labyrinth)

    def create_player(self):
        self.player = Player(self.game_labyrinth.exit_doorstep_coord, self.config['inventory'],  self.config['health'])

    def create_bear(self):
        self.bear = Player(self.game_labyrinth.get_free_cell(), {}, 1)

    def step_player(self, command):
        command_possible, command_respond = self.checker.check_command(command, self.player)
        print(command_respond)
        if command_respond == 'step executed, treasure':
            self.player.add_treasure()
            self.game_labyrinth.delete_treasure()
        if command_possible:
            if command == 'keep'or command == 'show map':
                coordinate_holes = self.game_labyrinth.dict_object['holes'].list_coordinates
                if list(self.player.coordinate_location) in [list(i) for i in coordinate_holes]:
                    print('teleport')
                    self.player.change_location_by_teleport(coordinate_holes)
                if command == 'show map':
                    self.show_map()
            else:
                self.player.change_sate_by_step(command)
            if command_respond == 'step executed, open exit':
                self.game_end = True
            river_coordinates = self.game_labyrinth.dict_object['river'].coordinates
            if list(self.player.coordinate_location) in [list(i) for i in river_coordinates]:
                self.player.change_coordimate_rier(river_coordinates)
            self.step_bear()

    def step_bear(self):
        command_possible = False
        while not command_possible:
            random_step_command = random.choice(list(step_by_command.keys()))
            command_possible, command_respond = self.checker.check_command(random_step_command, self.bear)
        if random_step_command == 'keep':
            coordinate_holes = self.game_labyrinth.dict_object['holes'].list_coordinates
            if list(self.bear.coordinate_location) in [list(i) for i in coordinate_holes]:
                self.bear.change_location_by_teleport(coordinate_holes)
        else:
            self.bear.change_sate_by_step(random_step_command)
        river_coordinates = self.game_labyrinth.dict_object['river'].coordinates
        if list(self.bear.coordinate_location) in [list(i) for i in river_coordinates]:
            self.bear.change_coordimate_rier(river_coordinates)

    def show_map(self):
        map_labyrinth = np.copy(self.game_labyrinth.map_labyrinth)
        coordin_player = self.player.coordinate_location
        coordin_bear = self.bear.coordinate_location
        map_labyrinth[coordin_player[0]][coordin_player[1]] = 'P'
        map_labyrinth[coordin_bear[0]][coordin_bear[1]] = 'B'
        print(map_labyrinth)

    def meet_bear(self):
        pass

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

