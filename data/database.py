
import numpy as np

step_by_command = {'go up':np.array((-2, 0)), 'go down':np.array((2, 0)), 
                     'go left':np.array((0, -2)), 'go right':np.array((0, 2)),
                     'keep':np.array((0, 0))}

dict_icon_labyrinth_object = {'wall':'W',
                              'monolith':'M',
                              'treasure':'T',
                              'hole':'H',
                              'exit':'E',
                              'free_cell': ' ',
                              'river':'R'}

next_cell = {'up':np.array((-1, 0)), 'down':np.array((1, 0)), 
                     'left':np.array((0, -1)), 'right':np.array((0, 1)),}

short_command_dict = {'u':'go up', 'd':'go down', 
                     'l':'go left', 'r':'go right',
                     'k':'keep'}

global_config_dict = {'max_labyrinth_size':10,
                      'min_labyrinth_size':4,
                      'num_holes':5}

standart_start_config = {'num_holes':5, 'inventory':[], 'objects':{}}

gameplay_possible_command = list(step_by_command.keys()) + ['finish', 'cheatcode', 'save'] + list(short_command_dict.keys())