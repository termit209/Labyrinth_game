
from data.database import *
from objects.Game import Game
from interface.CLI import CLInteface
from objects.Game import Game
from objects.Game import Game

test = 'CLI'

if test == 'lab':
    from objects.Labyrinth import Labyrinth
    test_lab = Labyrinth(6, {})
    test_lab.generate_monoliths()
    test_lab.generate_walls()
    test_lab.generate_exit()
    test_lab.generate_treasure()
    print(test_lab.map_labyrinth)
    test_lab.generate_warmholes(2)
    test_lab.generate_river(4)
    test_lab.delete_treasure()
    print(test_lab.map_labyrinth)
    #print(test_lab.dict_object['holes'].list_coordinates)

elif  test == 'player':
    from objects.Player import Player
    test_player = Player(np.array((3, 1)), [], 3)
    print(test_player.coordinate_location)
    test_player.change_sate_by_step('keep')
    print(test_player.coordinate_location)
    test_player.change_coordimate_river([(1, 1), (2, 1), (3, 1)])
    print(test_player.coordinate_location)

elif test == 'checker':
    from objects.Checker import Checker
    from objects.Player import Player
    from objects.Labyrinth import Labyrinth
    test_player = Player(np.array((1, 1)), [], 3)
    test_lab = Labyrinth(6, {})
    test_lab.generate_monoliths()
    test_lab.generate_walls()
    test_lab.generate_exit()
    test_checker = Checker(test_lab)
    print(test_lab.map_labyrinth)
    print(test_checker.check_command('go up', test_player))
   # test2_player = Player(np.array(test_lab.dict_object['treasure'].coordinate) - np.array((0, 2)), [])
    #print(test2_player.coordinate_location)
    #for command in  step_by_command.keys():
    #    print(command, test_checker.check_command(command, test2_player))

elif test == 'game':
    test_config = {'size':7, 'num_holes':3, 'inventory':[], 'objects':{}, 'health':3, 'lenght_river':4}
    test_game = Game(test_config)
    test_game.create_labyrinth()
    test_game.create_player()
    test_game.create_cheker()
    test_game.create_bear()
    print(test_game.show_map())
    command = ''
    while command != 'stop':
        command = input ()
        if command == 'm':
            test_game.show_map()
        else:
            test_game.step_player(command)


if test == "CLI":
    test_int = CLInteface()
    test_int.main_menu()