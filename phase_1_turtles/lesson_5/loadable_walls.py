from turtle import Screen
from maze_utils import convert_maze_to_coordinates, place_bricks

world = Screen()

with open("maze.txt") as maze_file:
    maze_string = maze_file.read()
    print(maze_string)
    maze = convert_maze_to_coordinates(maze_string)
    place_bricks(maze)

world.exitonclick()