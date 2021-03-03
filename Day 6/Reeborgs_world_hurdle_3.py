#The third hurdle challenge at https://reeborg.ca/

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not front_is_clear():
        jump()
    elif not wall_in_front():
        move()
    else:
        jump()

 
