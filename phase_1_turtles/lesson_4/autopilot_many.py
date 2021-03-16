from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape, random_coordinates

class TankAI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        set_custom_shape(self,tank_shape)
        self.color("magenta","yellow")
        self.penup()

    def drive_to_target(self, target:Turtle, speed:int=3) -> None:
        self.setheading(self.towards(target))
        self.forward(speed)
        ontimer(lambda:self.drive_to_target(target),100)

turtle_world = Screen()

tank = TankAI()
tank.goto(random_coordinates())

enemy_a = TankAI()
enemy_a.color("green","red")
enemy_a.goto(random_coordinates())
enemy_a.drive_to_target(tank)

enemy_b = TankAI()
enemy_b.color("green","orange")
enemy_b.goto(random_coordinates())
enemy_b.drive_to_target(tank)

enemy_c = TankAI()
enemy_c.color("green","blue")
enemy_c.goto(random_coordinates())
enemy_c.drive_to_target(tank)

turtle_world.exitonclick()