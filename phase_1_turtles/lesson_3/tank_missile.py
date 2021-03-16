from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape
from random import randint 

class Missile(Turtle):
    def __init__(self,rocket_speed:int,firing_range:int,wind_factor:int) -> None:
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.SPEED = rocket_speed
        self.RANGE = firing_range
        self.WIND = wind_factor
    
    def fly(self) -> None:
        self.forward(self.SPEED)
        self.right(randint(-self.WIND,self.WIND))        
        ontimer(self.fly,100) 


class Tank(Turtle):
    def __init__(self) -> None:
        super().__init__()
        set_custom_shape(self,tank_shape)
        self.color("magenta","yellow")
        self.penup()
        self.missile = Missile(3,300,1)

    def shoot(self) -> None:
        self.missile.hideturtle()
        self.missile.penup()
        self.missile.clear()
        self.missile.setpos(self.pos())
        self.missile.seth(self.heading())
        self.missile.showturtle()
        self.missile.pendown()
        self.missile.fly()

turtle_world = Screen()

tank = Tank()
tank.shoot()
tank.shoot()
tank.shoot()

turtle_world.exitonclick()