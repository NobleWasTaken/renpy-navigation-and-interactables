# The script of the game goes in this file.

# The game starts here.
label start:
    call init_all
    call play_intro
    call enter_game
    call play_ending
    return