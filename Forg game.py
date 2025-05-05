def jump():
    turn_left()
    move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go_down():
    move()


height = 0
is_turn_right = True
print(f"intial Height {height}")
while not at_goal():
    if front_is_clear():
        move()
        while height != 0:
            print(f"intial While loop Height {height}")
            if is_turn_right:
                turn_right()
                is_turn_right = False
            go_down()
            height -= 1
            print(height)
            if height == 0:
                turn_left()
    else:
        jump()
        height += 1
        is_turn_right = True
        print(f"Wall in front height {height}")