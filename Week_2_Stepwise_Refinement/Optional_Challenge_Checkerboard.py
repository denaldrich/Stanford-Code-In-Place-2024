from karel.stanfordkarel import *

def main():
    put_beeper()
    while left_is_clear():
        draw_row()
        junp_row() 
    draw_row()
    return_to_starting_point()
    
def draw_row():
    
    while front_is_clear():
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()    
        
def junp_row():
    turn_around()
    while front_is_clear():
        move()
    if beepers_present():
        turn_right()
        move()
        turn_right()
        if front_is_clear():
            move()
            put_beeper()
    else:
        turn_right()
        move()
        turn_right()
        put_beeper()
    
def return_to_starting_point():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
    

if __name__ == '__main__':
    main()
