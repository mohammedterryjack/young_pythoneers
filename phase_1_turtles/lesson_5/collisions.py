from turtle import Screen
from maze_utils import load_maze_from_file, place_bricks, buffer_coordinates
from tank_utils import Tank

world = Screen()
world.bgpic("marble.gif")
maze = load_maze_from_file("maze.txt")
place_bricks(maze)

maze = buffer_coordinates(maze,5)
#TODO
#collision_detected = lambda player: player.position in maze 

tank = Tank()
tank.goto(50,-50)
tank.register_controls_to_world(world)

world.listen()
world.exitonclick()