from turtle import Screen, Turtle

turtle_world = Screen()
turtle_world.bgcolor("pink")

robot = Turtle()
robot.shape("turtle")
robot.color("magenta","yellow")

robot.left(90) 

def tree(turtle:Turtle, depth:int, distance:float=80., branching_angle:float=30.) -> None:    
    if depth == 0: return
    
    turtle.forward(distance) 
    turtle.right(branching_angle) 
    tree(turtle, depth-1, .8*distance) 
    
    turtle.left( 2*branching_angle )   
    tree(turtle, depth-1, .8*distance) 
    
    turtle.right(branching_angle) 
    turtle.backward(distance) 
           
tree(robot, 7) 
turtle_world.exitonclick()