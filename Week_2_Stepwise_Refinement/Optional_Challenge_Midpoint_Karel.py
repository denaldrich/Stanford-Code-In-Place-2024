from karel.stanfordkarel import *


def main():
    go_to_bottom_right()
    draw_diagonal_line()
    go_to_bottom_left()
    find_middle_beeper()
    put_beeper_at_midpoint()
    go_to_bottom_right()
    clear_diagonal_line()
    go_to_midpoint()
    
def go_to_bottom_right():
    while front_is_clear():
        move()

def draw_diagonal_line():
    turn_around()
    while front_is_clear():
        put_beeper()
        move()
        put_beeper()
        turn_right()
        move()
        turn_left()
    put_beeper()

def go_to_bottom_left():
    turn_left()
    while front_is_clear():
        move()
    turn_left()    
   
def find_middle_beeper():
    while no_beepers_present():
        move()
        turn_left()
        move()
        turn_right()

def put_beeper_at_midpoint():
    turn_right()
    while front_is_clear():
        move()
    put_beeper()
    turn_left()

def clear_diagonal_line():
    turn_around()
    while front_is_clear():
        pick_beeper()
        move()
        pick_beeper()
        turn_right()
        move()
        turn_left()
    pick_beeper()

def go_to_midpoint():
    go_to_bottom_left()
    while no_beepers_present():
        move()

def turn_around():
    turn_left()
    turn_left()
 
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program()
