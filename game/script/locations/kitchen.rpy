label enter_kitchen:
    $ kitchen.load()

screen kitchen:
    imagebutton:
        xpos 1504
        ypos 0
        idle "kitchen/livingroom_door_idle.png"
        hover "kitchen/livingroom_door_hover.png"
        action SetVariable("current_room", "livingroom"), Jump("update_gamestate")