label enter_kitchen:
    $ kitchen.load()

screen kitchen:
    imagebutton:
        xpos 1504
        ypos 0
        idle "kitchen/livingroom_door_idle.png"
        hover "kitchen/livingroom_door_hover.png"
        action Jump("kitchen_to_livingroom")

label kitchen_to_livingroom:
    $ current_room = "livingroom"
    jump update_gamestate