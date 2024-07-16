
screen bedroom:
    imagebutton:
        xpos 479
        ypos 478
        idle "bedroom/bed_idle.png"
        hover "bedroom/bed_hover.png"
        action Jump("test")

    imagebutton:
        xpos 882
        ypos 858
        idle "bedroom/arrow_idle.png"
        hover "bedroom/arrow_hover.png"
        action Call("test")

label test:
    "test"
    jump enter_game
    return

# var: room_name?
# var: screen_name
# var: background day
# var: background evening
# var: background night
# var: reactions to entrance?
# maybe do it as an array of strings, each one being to a label/function 
# that reacts to entering that specific room and has it's own checks to see 
# if it should play or not
# maybe something similar for interactible objects

# init python:
#     class scene:
#         # constructor called upon initialization of object
#         def __init__(self, scene_name, screen_name, bg_day, bg_evening, bg_night):
#             self.scene_name = scene_name
#             self.screen_name = screen_name
#             self.bg_day = bg_day
#             self.bg_evening = bg_evening
#             self.bg_night = bg_night

#         def load(self):
#             # select relevant bg according to time of day
#             if time_of_day == 1:
#                 bg = self.bg_day
#             elif time_of_day == 2:
#                 bg = self.bg_evening
#             else:
#                 bg = self.bg_night
            
#             # load scene
#             renpy.scene(bg)
#             renpy.call_screen(self.screen_name)

# label enter_game:
#     scene bg bedroom_day
#     call screen bedroom