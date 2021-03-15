from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape, random_coordinates
from typing import Tuple

class TankAI(Turtle):
    def __init__(
        self, 
        colours:Tuple[str,str] = ("magenta","yellow"),
        starting_position:Tuple[int,int]=(0,0),
        custom_shape:callable=tank_shape
    ) -> None:

        super().__init__()
        set_custom_shape(self,custom_shape)
        self.color(*colours)
        self.penup()
        self.goto(starting_position)

    def drive_to_target(self, target:Turtle, speed:int=3) -> None:
        new_heading = self.towards(target)
        self.setheading(new_heading)
        self.forward(speed)
        ontimer(lambda:self.drive_to_target(target),100)
    
turtle_world = Screen()

tank = TankAI(starting_position=random_coordinates())

enemy_a = TankAI(("green","red"),random_coordinates())
enemy_b = TankAI(("green","orange"),random_coordinates())
enemy_c = TankAI(("green","blue"),random_coordinates())

enemy_a.drive_to_target(tank)
enemy_b.drive_to_target(tank)
enemy_c.drive_to_target(tank)

turtle_world.exitonclick()