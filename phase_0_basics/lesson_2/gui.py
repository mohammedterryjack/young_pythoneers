from turtle import Screen 
from utils import say 

background_window = Screen()
background_window.title("text to speech")
background_window.setup(330,250)
background_window.bgcolor("light blue")

run = True
while run:
    message = background_window.textinput("Hear me speak","What would you like me to say?")
    run = message is not None
    if not run: message = "good bye"
    say(message,"windows")