label enter_bedroom:
    $ bedroom.load_scene()

screen bedroom:
    imagebutton:
        xpos 479
        ypos 478
        idle "bedroom/bed_idle.png"
        hover "bedroom/bed_hover.png"
        action Call("pass_time")

    imagebutton:
        xpos 882
        ypos 858
        idle "bedroom/arrow_idle.png"
        hover "bedroom/arrow_hover.png"
        action Call("bedroom_to_livingroom")

label pass_time:
    "pass time"
    jump enter_game
    return

label bedroom_to_livingroom:
    $ current_room = "livingroom"
    jump update_gamestate
    return