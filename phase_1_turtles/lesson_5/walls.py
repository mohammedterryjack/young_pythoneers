from turtle import Screen
from maze_utils import convert_maze_to_coordinates, place_bricks

LEVEL_1 = """
XXXXXX
XX  XX
XXX XX
XXX XX
XXX XX
XXXXXX
"""
LEVEL_2 = """
XXXXXX
X.   X
XXXX X
X    X
X XXXX
X    X
XXXXXX 
"""
    
world = Screen()

maze = convert_maze_to_coordinates(LEVEL_1)
place_bricks(maze)

world.exitonclick()