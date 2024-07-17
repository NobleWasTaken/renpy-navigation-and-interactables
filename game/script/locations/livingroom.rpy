screen livingroom:
    imagebutton:
        xpos 1108
        ypos 50
        idle "livingroom/bedroom_door_idle.png"
        hover "livingroom/bedroom_door_hover.png"
        action Call("pass_time")

    imagebutton:
        xpos 344
        ypos 72
        idle "livingroom/kitchen_door_idle.png"
        hover "livingroom/kitchen_door_hover.png"
        action Call("test")

# label pass_time:
#     "pass time"
#     jump enter_game
#     return

# label test:
#     "test"
#     jump enter_game
#     return