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
        world.onkey(lambda:self.shoot(3,300,1),shoot)

    def shoot(self,rocket_speed:int,firing_range:int,wind_factor:int) -> None:
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
turtle_world.bgcolor("pink")

tank = Tank()
tank.register_controls_to_world(turtle_world)

turtle_world.listen()
turtle_world.exitonclick()