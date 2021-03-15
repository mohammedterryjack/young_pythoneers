from turtle import register_shape, Turtle
from typing import Tuple
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

def random_coordinates() -> Tuple[int,int]:
    return (
        randint(-100,100),
        randint(-100,100)
    )
