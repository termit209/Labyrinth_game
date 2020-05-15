
import random
import numpy as np
from data.database import dict_icon_labyrinth_object

#dict_icon_labyrinth_object = {'wall':'W',
#                              'monolith':'M',
#                              'treasure':'T',
#                              'hole':'H',
#                              'exit':'E'}

class River():
    def __init__(self, list_coordinates):
        self.list_coordinates =  list_coordinates
        self.source = list_coordinates[0]
        self.end = list_coordinates[-1]

class Wormholes:
    def __init__(self, num_holes, list_coordinates):
        self.num_holes = num_holes
        self.list_coordinates = list_coordinates


class Treasure:
    def __init__(self, coordinate):
        self.coordinate = coordinate


class Labyrinth():
    def __init__(self, size, dict_objects):
        self.size = size
        self.matrix_size = size*2 + 1
        self.map_labyrinth = np.full((2*size+1, 2*size+1), ' ')
        self.dict_object = dict_objects

    def generate_wals(self):
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if (i == 0) or (j == 0) or (i == self.matrix_size-1) or (j == self.matrix_size-1):
                    self.map_labyrinth[i][j] = dict_icon_labyrinth_object['monolith']
                elif (j < self.matrix_size-2) and (i%2==0):
                    self.map_labyrinth[i][j] = dict_icon_labyrinth_object['wall']
     
    def generate_exit(self):
        doorstep_in_wall = True
        while doorstep_in_wall:
            coordinate_exit = random.randrange(1, self.size*2, 2)
            choised_wall = random.choice([('left', (coordinate_exit, 0),  (coordinate_exit, 1)),
                                            ('right',  (coordinate_exit, self.size*2),  (coordinate_exit, self.size*2-1)), 
                                            ('upper',  (self.size*2, coordinate_exit),  (self.size*2-1, coordinate_exit)),
                                            ('bottom',  (0, coordinate_exit),  (1, coordinate_exit))])
            doorstep_coordinate = choised_wall[2]
            doorstep_in_wall = self.map_labyrinth[doorstep_coordinate[0]][doorstep_coordinate[1]] == dict_icon_labyrinth_object['wall']
        self.exit_doorstep_coord = doorstep_coordinate
        self.exit_coord = choised_wall[1]
        self.map_labyrinth[self.exit_coord[0]][self.exit_coord[1]] = dict_icon_labyrinth_object['exit']

    def generate_treasure_coordinate(self):
        treasure_in_wall = True
        while treasure_in_wall:
            x_coordinate, y_coordinate = self.get_random_cell()
            treasure_in_wall = self.map_labyrinth[x_coordinate][y_coordinate] == dict_icon_labyrinth_object['wall']
        self.map_labyrinth[x_coordinate][y_coordinate] = dict_icon_labyrinth_object['treasure']
        self.dict_object['treasure'] = Treasure((x_coordinate, y_coordinate))

    def generate_warmHoles(self, num_holes):
        hole_coordinate_list = []
        for index_hole in range(num_holes):
            hole_in_treasure = True
            overlap_holes = True
            while hole_in_treasure or overlap_holes:
                x_coordinate, y_coordinate = self.get_random_cell()
                hole_in_treasure = self.map_labyrinth[x_coordinate][y_coordinate] == dict_icon_labyrinth_object['treasure']
                overlap_holes = 'H' in self.map_labyrinth[x_coordinate][y_coordinate] 
            self.map_labyrinth[x_coordinate][y_coordinate] = dict_icon_labyrinth_object['hole']
            hole_coordinate_list.append((x_coordinate, y_coordinate))
        self.dict_object['holes'] = Wormholes(num_holes, hole_coordinate_list)
    
    def get_random_cell(self):
        x_coordinate = random.randrange(1, self.matrix_size-1, 2)
        y_coordinate = random.randrange(1, self.matrix_size-1, 2)
        return (x_coordinate, y_coordinate)

    def get_free_cell(self):
        coordinate = (0, 0)
        while not self.is_cell_free(coordinate):
            coordinate = self.get_random_cell()
        return coordinate

    def give_labyrinth_state(self):
        pass
    
    #def generate_river(self, lenght_river):
    #    coordinates = [self.get_free_cell()]
    #    current_lenght = len(coordinates)
    #    dirrections = ['up', 'down', 'right', 'left']
    #    while current_lenght < lenght_river:
    #        random.shuffle(dirrections)
    #        for dirrection in dirrections:
                

    def is_cell_free(self, coordinate):
        return self.map_labyrinth[coordinate[0]][coordinate[1]] == ' '


if __name__ == '__main__':
    test_lab = Labyrinth(2, {})
    test_lab.generate_wals()
    test_lab.generate_exit()
    test_lab.generate_treasure_coordinate()
    test_lab.generate_warmHoles(2)
    print(test_lab.map_labyrinth)
    print(test_lab.dict_object['holes'].list_coordinates)
