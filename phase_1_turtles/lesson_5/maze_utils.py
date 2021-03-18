from turtle import Turtle,Screen
from typing import Tuple, Iterator, Set

def convert_maze_to_coordinates(maze:str, wall:str="X", scale:int=30) -> Iterator[Tuple[int,int]]:
    rows = maze.split("\n")
    for row_index,row in enumerate(rows):
        for column_index,cell in enumerate(row):
            if cell == wall:
                yield (
                    column_index*scale,
                    -row_index*scale
                )

def place_brick(x:int,y:int) -> None:
    wall = Turtle()
    wall.hideturtle()
    wall.penup()
    wall.shape("square")
    wall.speed("fastest")
    wall.goto(x,y)
    wall.showturtle()

def place_bricks(coordinates:Set[Tuple[int,int]]) -> None:
    for coordinate in coordinates:
        place_brick(*coordinate)

def load_maze_from_file(filename:str) -> Set[Tuple[int,int]]:
    with open(filename) as maze_file:
        return set(convert_maze_to_coordinates(maze_file.read()))

# def buffer_coordinates(coordinates:Set[Tuple[int,int]],buffer_radius:int) -> Set[Tuple[int,int]]:
#     buffer_coordinates = set()
#     for x,y in coordinates:
#         for buffer in range(buffer_radius):
#             buffer_coordinates |= {
#                 (x+buffer,y+buffer),
#                 (x-buffer,y-buffer)
#             }
#     return coordinates | buffer_coordinates