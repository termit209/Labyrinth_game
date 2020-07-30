
import numpy as np

step_by_command = {'go up':np.array((-1, 0)), 'go down':np.array((1, 0)), 
                     'go left':np.array((0, -1)), 'go right':np.array((0, 1)),
                     'keep':np.array((0, 0)), 'show map':np.array((0, 0))}

dict_icon_labyrinth_object = {'wall':'W',
                              'monolith':'M',
                              'treasure':'T',
                              'hole':'H',
                              'exit':'E',
                              'free_cell': ' ',
                              'river':'R',
                              'bear':'B',
                              'player':'P'}

next_cell = {'up':np.array((-1, 0)), 'down':np.array((1, 0)), 
                     'left':np.array((0, -1)), 'right':np.array((0, 1)),}

short_command_dict = {'u':'go up', 'd':'go down', 
                     'l':'go left', 'r':'go right',
                     'k':'keep', 'm':'show map'}

global_config_dict = {'max_labyrinth_size':10,
                      'min_labyrinth_size':4,
                      'num_holes':5}

standart_start_config = {'num_holes':5, 'inventory':[], 'objects':{}, 'lenght_river':4, 'health':3}

gameplay_possible_command = list(step_by_command.keys()) + ['finish', 'cheatcode', 'save'] + list(short_command_dict.keys())

action_respond_message = {}

#smile = {
#' (>_<) ' + '\n', 
#'(^_-)' + '\n', 
#'\(^_^)/ ', 'Congratulation ', sep='\n'
#'(╯︵╰,) ', 'Lose, try again next time ', sep='\n'
#'\n', '(^_^)/'
#'(u_u)/'
#'(^_^)?'
#}

start_menu_command = ['start', 'load', 'finish']
