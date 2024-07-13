# The script of the game goes in this file.

# The game starts here.
label start:
    call init_all
    call play_intro
    call enter_game
    call play_ending
    return

label init_all:
    return

label enter_game:
    scene bg bedroom_day
    call screen bedroom

screen bedroom:
    imagebutton:
        xpos 479
        ypos 478
        idle "bedroom_bed_idle.png"
        hover "bedroom_bed_hover.png"
        action Jump("test")

    imagebutton:
        xpos 882
        ypos 858
        idle "bedroom_arrow_idle.png"
        hover "bedroom_arrow_hover.png"
        action Jump("test")

label test:
    "test"
    jump enter_game
