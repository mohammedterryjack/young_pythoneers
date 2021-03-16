from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape, random_coordinates
from typing import Tuple
from tank_missile_controls_ai import Tank

turtle_world = Screen()
turtle_world.bgcolor("pink")

tank = Tank()
tank.register_controls_to_world(turtle_world)

for _ in range(3):
    enemy = Tank()
    enemy.color("green","red")
    enemy.goto(random_coordinates())
    enemy.drive_to_target_and_shoot(tank)

turtle_world.listen()
turtle_world.exitonclick()