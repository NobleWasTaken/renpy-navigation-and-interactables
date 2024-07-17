label enter_livingroom:
    $ livingroom.load()

screen livingroom:
    imagebutton:
        xpos 1108
        ypos 50
        idle "livingroom/bedroom_door_idle.png"
        hover "livingroom/bedroom_door_hover.png"
        action Jump("livingroom_to_bedroom")

    imagebutton:
        xpos 344
        ypos 72
        idle "livingroom/kitchen_door_idle.png"
        hover "livingroom/kitchen_door_hover.png"
        action Jump("livingroom_to_kitchen")

label livingroom_to_bedroom:
    $ current_room = "bedroom"
    jump update_gamestate

label livingroom_to_kitchen:
    $ current_room = "kitchen"
    jump update_gamestate