label enter_livingroom:
    $ livingroom.load_scene()

screen livingroom:
    imagebutton:
        xpos 1108
        ypos 50
        idle "livingroom/bedroom_door_idle.png"
        hover "livingroom/bedroom_door_hover.png"
        action Call("livingroom_to_bedroom")

    imagebutton:
        xpos 344
        ypos 72
        idle "livingroom/kitchen_door_idle.png"
        hover "livingroom/kitchen_door_hover.png"
        action Call("test")

label livingroom_to_bedroom:
    $ current_room = "bedroom"
    jump update_gamestate

label test:
    "test"
    jump enter_game
    return