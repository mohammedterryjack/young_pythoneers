from typing import List, Optional
from pynput.keyboard import Key, Listener
from time import sleep

class PlayerInput(Exception): pass

def on_press(key) -> None:

    if key.char in ("w","a","s","z"):
        raise PlayerInput(key)
    
def update_direction(direction:str) -> None:
    print(direction)
    
with Listener(on_press) as listener:
    try:
        listener.join()
    except PlayerInput as player_key:
        update_direction(player_key.args[0])
