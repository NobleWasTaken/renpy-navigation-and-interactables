label enter_bedroom:
    $ bedroom.load()

screen bedroom:
    imagebutton:
        xpos 479
        ypos 478
        idle "bedroom/bed_idle.png"
        hover "bedroom/bed_hover.png"
        action Jump("pass_time")

    imagebutton:
        xpos 882
        ypos 858
        idle "bedroom/arrow_idle.png"
        hover "bedroom/arrow_hover.png"
        action SetVariable("current_room", "livingroom"), Jump("update_gamestate")

label pass_time:
    $ time_of_day = time_of_day + 1
    if time_of_day > 3:
        $ time_of_day = 1;
    jump update_gamestate