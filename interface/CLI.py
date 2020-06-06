
from  objects.Player import  Player
from objects.Game import Game
from data.database import *


class CLInteface:
    start_menu_command = ['start', 'load', 'finish']
    def __init__(self):
        pass
    
    def check_user_input(self, list_possible_command):
        user_input = input()
        while user_input not in list_possible_command:
            print(' (>_<) ')
            print(user_input + ' is wrong command, try again a one from: ' + str(list_possible_command))
            user_input = input()
        return user_input
    
    def game_interface(self):
        print('(^_^)?')
        print("Type labyrinth size from 4 to 10.")
        size_list = list(range(global_config_dict['min_labyrinth_size'], global_config_dict['max_labyrinth_size']+1))
        standart_start_config['size'] = int(self.check_user_input([str(i) for i in size_list]))
        game = Game(standart_start_config)
        game.create_game()
        game_finish = False
        while not game_finish:
            command = self.check_user_input(gameplay_possible_command)
            if command == 'cheatcode':
                print('(^_-)' + '\n')
                game.show_map()
            elif command == 'save':
                pass
            elif command == 'finish':
                game_finish = True
            elif command in short_command_dict:
                game.turn(short_command_dict[command])
            else:
                game.turn(command)
            game_finish |= game.game_end
        if game.game_result == 'win':
            print('\(^_^)/ ', 'Congratulation ', sep='\n')
        else:
            print('(╯︵╰,) ', 'Lose, try again next time ', sep='\n')

    def main_menu(self):
        print('\n', '(^_^)/')
        print("Hello player!")
        print("Print 'start' to start new game or 'load' to load previous game.")
        main_menu_command = self.check_user_input(self.start_menu_command)
        if main_menu_command == 'start':
            self.game_interface()
        elif main_menu_command == 'load':
            pass
        else:
            print('(u_u)/', 'See you again!')
