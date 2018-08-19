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
        'J at (2, 3) ate 2 sprouts.'
        """
        return "{} at ({}, {}) ate {} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
