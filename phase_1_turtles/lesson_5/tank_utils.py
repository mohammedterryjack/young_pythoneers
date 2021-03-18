from turtle import Screen, Turtle, ontimer, register_shape
from random import randint 

def set_custom_shape(pen:Turtle,turtle_movements:callable,shape_name:str="custom") -> None:
    pen.speed("fastest")
    pen.hideturtle()
    pen.begin_poly() 
    turtle_movements(pen)
    pen.end_poly() 
    register_shape(shape_name, pen.get_poly()) 
    pen.reset()
    pen.shape(shape_name)
    pen.speed("slowest")

def tank_shape(turtle:Turtle) -> None:
    turtle.right(90)
    turtle.backward(5)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(3)
    turtle.forward(2)
    turtle.right(180)
    for _ in range(2):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.right(90)
    turtle.forward(10)
    turtle.circle(4)

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
               
    def drive_to_target_and_shoot(self, target:Turtle, speed:int=1) -> None:
        if self.distance(target) <= 50: 
            self.shoot(speed)
        else:
            self.setheading(self.towards(target))
            self.forward(speed)
            ontimer(lambda:self.drive_to_target_and_shoot(target),100)