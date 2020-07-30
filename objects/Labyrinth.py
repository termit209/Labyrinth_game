
import random
import numpy as np

from data.database import dict_icon_labyrinth_object, next_cell


class River:
    def __init__(self, lenght_river, list_coordinates):
        self.list_coordinates =  list_coordinates
        self.source = list_coordinates[0]
        self.end = list_coordinates[-1]
        self.lenght_river = lenght_river


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
        self.matrix_size = size + 2
        self.map_labyrinth = np.full((self.matrix_size, self.matrix_size), dict_icon_labyrinth_object['free_cell'])
        self.dict_object = dict_objects

    def generate_monoliths(self):
        for i in range(self.matrix_size):
            self.map_labyrinth[i][0] = dict_icon_labyrinth_object['monolith']
            self.map_labyrinth[i][self.matrix_size-1] = dict_icon_labyrinth_object['monolith']
        for j in range(self.matrix_size):
            self.map_labyrinth[0][j] = dict_icon_labyrinth_object['monolith']
            self.map_labyrinth[self.matrix_size-1][j] = dict_icon_labyrinth_object['monolith']

    def generate_walls(self):
        for wall_size in range(1, self.size):
            if wall_size % 2 == 1:
                for i in range(wall_size):
                    self.map_labyrinth[1+i][wall_size+1] = dict_icon_labyrinth_object['wall']
            else:
                for j in range(wall_size):
                    self.map_labyrinth[wall_size+1][1+j] = dict_icon_labyrinth_object['wall']
    
    def generate_exit(self):
        doorstep_in_wall = True
        while doorstep_in_wall:
            coordinate_exit = random.randrange(1, self.size+1)
            choised_wall = random.choice([('left', np.array((coordinate_exit, 0)), np.array((coordinate_exit, 1))),
                                            ('right', np.array((coordinate_exit, self.size+1)), np.array((coordinate_exit, self.size))), 
                                            ('bottom', np.array((self.size+1, coordinate_exit)), np.array((self.size, coordinate_exit))),
                                            ('upper', np.array((0, coordinate_exit)), np.array((1, coordinate_exit)))])
            doorstep_coordinate = choised_wall[2]
            doorstep_in_wall = self.map_labyrinth[doorstep_coordinate[0]][doorstep_coordinate[1]] == dict_icon_labyrinth_object['wall']
        self.exit_doorstep_coord = doorstep_coordinate
        self.exit_coord = choised_wall[1]
        self.map_labyrinth[self.exit_coord[0]][self.exit_coord[1]] = dict_icon_labyrinth_object['exit']

    def generate_treasure(self):
        (x_coordinate, y_coordinate) = self.get_free_cell()
        self.map_labyrinth[x_coordinate][y_coordinate] = dict_icon_labyrinth_object['treasure']
        self.dict_object['treasure'] = Treasure((x_coordinate, y_coordinate))

    def generate_warmholes(self, num_holes):
        hole_coordinate_list = []
        for index_hole in range(num_holes):
            random_free_cell = self.get_free_cell()
            self.map_labyrinth[random_free_cell[0]][random_free_cell[1]] = dict_icon_labyrinth_object['hole']
            hole_coordinate_list.append(random_free_cell)
        self.dict_object['holes'] = Wormholes(num_holes, hole_coordinate_list)
    
    def get_random_cell(self):
        x_coordinate = random.randrange(1, self.size+1)
        y_coordinate = random.randrange(1, self.size+1)
        return np.array((x_coordinate, y_coordinate))

    def get_free_cell(self):
        coordinate = np.array((0, 0))
        while not self.is_cell_free(coordinate):
            coordinate = self.get_random_cell()
        return coordinate

    def give_labyrinth_state(self):
        pass
    
    def generate_river(self, lenght_river):
        coordinates = [self.get_free_cell()]
        dirrections = list(next_cell.keys())
        while len(coordinates) <= lenght_river:
            random.shuffle(dirrections)
            for dirrection in dirrections:
                last_coordinate = coordinates[-1]
                candidate_coordinate = last_coordinate + next_cell[dirrection]
                if self.is_cell_free(candidate_coordinate):
                    coordinates.append(candidate_coordinate)
                    break
            else:
                coordinates = [self.get_free_cell()]
        for river_cell in coordinates:
            self.map_labyrinth[river_cell[0]][river_cell[1]] = dict_icon_labyrinth_object['river']
        self.dict_object['river'] = River(lenght_river, coordinates)

    def is_cell_free(self, coordinate):
        return self.map_labyrinth[coordinate[0]][coordinate[1]] == dict_icon_labyrinth_object['free_cell']

    def delete_treasure(self):
        coordinate_treasure = self.dict_object['treasure'].coordinate
        self.map_labyrinth[coordinate_treasure[0]][coordinate_treasure[1]] = dict_icon_labyrinth_object['free_cell']
        self.dict_object.pop('treasure')

    def get_labyrinth_map(self):
        return np.copy(self.map_labyrinth)

    def get_doorstep_coord(self):
        return self.exit_doorstep_coord