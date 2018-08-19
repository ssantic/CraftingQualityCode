# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """(Rat, str, int, int) -> NoneType

        Initialise a Rat

        >>> rat = Rat('P', 2, 3)
        >>> rat.symbol
        'P'
        >>> rat.row
        2
        >>> rat.col
        3
        >>> rat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """(Rat, int, int) -> NoneType

        Set the location for the Rat in the Maze

        >>> rat = Rat('P', 2, 3)
        >>> rat.set_location(4, 5)
        >>> rat.row
        4
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """(Rat) -> NoneType

        Eat a sprout in the Maze

        >>> rat = Rat('P', 2, 3)
        >>> rat.num_sprouts_eaten
        0
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str

        Print information about the Rat

        >>> rat = Rat('P', 2, 3)
        >>> print(rat)
        P at (2, 3) ate 0 sprouts.
        """
        return "{} at ({}, {}) ate {} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize the maze's four instance variables:

        maze - contents of maze (walls, sprouts etc)
        rat_1 - first rat
        rat_2 - second rat
        num_sprouts_left - number of uneaten sprouts

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))
        >>> maze.maze[0][1]
        '#'
        >>> maze.maze[2][1]
        '@'
        >>> maze.rat_1.row
        1
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        for element in sum(self.maze, []):
            if element == SPROUT:
                self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """(Maze, int, int) -> bool

        Check whether the field in the Maze is a wall

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))

        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(1, 1)
        False
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str

        Return the character in the Maze at the given row and column

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))

        >>> maze.get_character(0, 0)
        '#'
        >>> maze.get_character(1, 1)
        'J'
        """
        if (self.rat_1.row == row and self.rat_1.col == col):
            return self.rat_1.symbol
        elif (self.rat_2.row == row and self.rat_2.col == col):
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """(Maze, Rat, int, int) -> bool
        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 2, 2)
        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         rat_1,\
                         rat_2)
        >>> maze.move(rat_1, DOWN, NO_CHANGE)
        True
        >>> rat_1.num_sprouts_eaten
        1
        """
        new_position = (rat.row + vertical, rat.col + horizontal)

        if self.is_wall(new_position[0], new_position[1]):
            return False
        else:
            if self.get_character(new_position[0], new_position[1]) == SPROUT:
                rat.eat_sprout()
                self.maze[new_position[0]][new_position[1]] = HALL
                self.num_sprouts_left -= 1
            rat.set_location(new_position[0], new_position[1])
            return True

    def __str__(self):
        """(Maze) -> str
        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 2, 2)
        >>> maze = Maze([['#','#','#','#'],\
                         ['#','.','.','#'],\
                         ['#','@','.','#'],\
                         ['#','#','#','#']],\
                         rat_1,\
                         rat_2)
        >>> print(maze)
        ####
        #J.#
        #@P#
        ####
        J at (1, 1) ate 0 sprouts.
        P at (2, 2) ate 0 sprouts.
        """

        result = ''
        for irow in range(len(self.maze)):
            for icol in range(len(self.maze[irow])):
                result += self.get_character(irow, icol)
            result += '\n'
        result += self.rat_1.__str__()
        result += '\n'
        result += self.rat_2.__str__()

        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

