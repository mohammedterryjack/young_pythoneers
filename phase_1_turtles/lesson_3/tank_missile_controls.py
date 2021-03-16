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

    def register_controls_to_world(
        self, world:Screen, 
        up:str="Up",down:str="Down",
        left:str="Left",right:str="Right",
        shoot:str="space",speed:int=3
    ) -> None:
        world.onkeypress(lambda:self.forward(speed),up) 
        world.onkeypress(lambda:self.backward(speed),down) 
        world.onkeypress(lambda:self.left(speed),left) 
        world.onkeypress(lambda:self.right(speed),right) 
        world.onkey(lambda:self.shoot(speed),shoot)
        

turtle_world = Screen()
turtle_world.bgcolor("pink")

tank = Tank()
tank.register_controls_to_world(turtle_world)

turtle_world.listen()
turtle_world.exitonclick()