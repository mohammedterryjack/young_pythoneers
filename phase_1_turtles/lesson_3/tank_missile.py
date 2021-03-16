from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape
from random import randint 

class Missile(Turtle):
    def __init__(self,rocket_speed:int,wind_factor:int=1) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.SPEED = rocket_speed
        self.WIND = wind_factor
    
    def fly(self) -> None:
        self.showturtle()
        self.pendown()
        self.forward(self.SPEED)
        self.right(randint(-self.WIND,self.WIND))        
        ontimer(self.fly,100) 


class Tank(Turtle):
    def __init__(self) -> None:
        super().__init__()
        set_custom_shape(self,tank_shape)
        self.color("magenta","yellow")
        self.penup()

    def shoot(self,speed:int) -> None:
        missile = Missile(speed)
        missile.setposition(self.position())
        missile.setheading(self.heading())
        missile.fly()

turtle_world = Screen()

tank = Tank()
tank.shoot(10)

turtle_world.exitonclick()