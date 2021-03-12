from turtle import Screen, Turtle
from utils import set_custom_shape, tank_shape


class Tank(Turtle):
    def __init__(self) -> None:
        super().__init__()
        set_custom_shape(self,tank_shape)
        self.color("magenta","yellow")
        self.penup()
    

turtle_world = Screen()
tank = Tank()
turtle_world.exitonclick()