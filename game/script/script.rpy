# The script of the game goes in this file.

# The game starts here.
label start:
    # init needed data
    call init_game

    # plays the intro sequence
    call play_intro

    # enters the game proper
    call update_gamestate

    # plays the ending sequence
    call play_ending

    return

label init_game:
    define config.window = Hide
    default time_of_day = 1
    default current_room = "bedroom"
    call init_locations
    return

label update_gamestate:
    call expression "enter_" + current_room
    return