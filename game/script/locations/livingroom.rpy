label enter_livingroom:
    $ livingroom.load()

screen livingroom:
    imagebutton:
        xpos 1108
        ypos 50
        idle "livingroom/bedroom_door_idle.png"
        hover "livingroom/bedroom_door_hover.png"
        action SetVariable("current_room", "bedroom"), Jump("update_gamestate")

    imagebutton:
        xpos 344
        ypos 72
        idle "livingroom/kitchen_door_idle.png"
        hover "livingroom/kitchen_door_hover.png"
        action SetVariable("current_room", "kitchen"), Jump("update_gamestate")