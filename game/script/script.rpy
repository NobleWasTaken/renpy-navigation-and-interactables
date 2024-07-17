# The script of the game goes in this file.

# The game starts here.
label start:
    # init needed data
    call init_all

    # plays the intro sequence
    call play_intro

    # enters the game proper
    call enter_game

    # plays the ending sequence
    call play_ending

    return

label init_all:
    default time_of_day = 3
    define config.window = Hide
    call init_locations
    return

label enter_game:
    $ livingroom.load_scene()