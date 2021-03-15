from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape
from random import randint 
from typing import Tuple

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
        self.missile = Missile(3,300,1)

    def register_controls_to_world(
        self, world:Screen, 
        up:str="Up",down:str="Down",
        left:str="Left",right:str="Right",
        shoot:str="space"
    ) -> None:
        world.onkeypress(lambda:self.forward(1),up) 
        world.onkeypress(lambda:self.backward(1),down) 
        world.onkeypress(lambda:self.left(1),left) 
        world.onkeypress(lambda:self.right(1),right) 
        world.onkey(self.shoot,shoot)

    def shoot(self) -> None:
        self.missile.hideturtle()
        self.missile.penup()
        self.missile.clear()
        self.missile.setpos(self.pos())
        self.missile.seth(self.heading())
        self.missile.showturtle()
        self.missile.pendown()
        self.missile.fly()

    def drive_to_target(self, target:Turtle, speed:int=1) -> None:
        if self.distance(target) <= 50: self.shoot()
        else:
            new_heading = self.towards(target)
            self.setheading(new_heading)
            self.forward(speed)
            ontimer(lambda:self.drive_to_target(target),100)