from turtle import Screen, Turtle
from utils import set_custom_shape, tank_shape
from random import randint 

class Tank(Turtle):
    def __init__(self) -> None:
        super().__init__()
        set_custom_shape(self,tank_shape)
        self.color("magenta","yellow")
        self.penup()
        self.missile = Turtle()
        self.missile.speed("fastest")
        self.missile.hideturtle()

    def shoot(self,rocket_speed:int=2,firing_range:int=300,wind_factor:int=1) -> None:
        self.missile.hideturtle()
        self.missile.penup()
        self.missile.clear()
        self.missile.setpos(self.pos())
        self.missile.seth(self.heading())
        self.missile.showturtle()
        self.missile.pendown()
        for _ in range(firing_range):
            self.missile.forward(rocket_speed)
            self.missile.right(randint(-wind_factor,wind_factor))
        


turtle_world = Screen()

tank = Tank()
tank.shoot()
tank.shoot()
tank.shoot()

turtle_world.exitonclick()