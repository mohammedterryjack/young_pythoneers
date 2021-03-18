from turtle import Screen
from maze_utils import load_maze_from_file, place_bricks
from tank_utils import Tank

world = Screen()
world.bgpic("marble.gif")
maze = load_maze_from_file("maze.txt")
place_bricks(maze)

team_1_player_1 = Tank()
team_1_player_1.goto(50,-50)
team_1_player_1.register_controls_to_world(world)

team_2_player_2 = Tank()
team_2_player_2.color("green","red")
team_2_player_2.goto(150,-150)
team_2_player_2.register_controls_to_world(
    world, shoot="q",
    up="w",down="z",
    left="a",right="d",
)

team_2_bot = Tank()
team_2_bot.color("blue","orange")
team_2_bot.goto(50, -150)
team_2_bot.drive_to_target_and_shoot(team_1_player_1)

world.listen()
world.exitonclick()