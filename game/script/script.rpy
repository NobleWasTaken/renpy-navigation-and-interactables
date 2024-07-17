# The script of the game goes in this file.

# init python:
#     class location:
#         # constructor called upon initialization of object
#         def __init__(self, scene_name, screen_name, bg_day, bg_evening, bg_night):
#             self.scene_name = scene_name
#             self.screen_name = screen_name
#             self.bg_day = bg_day
#             self.bg_evening = bg_evening
#             self.bg_night = bg_night

#         # returns the correct bg according to time of day
#         def get_current_bg(self):
#             if time_of_day == 1:
#                 bg = self.bg_day
#             elif time_of_day == 2:
#                 bg = self.bg_evening
#             else:
#                 bg = self.bg_night
#             return bg

#         # load the location
#         def load_scene(self):
#             renpy.scene()
#             renpy.show(self.get_current_bg())
#             renpy.call_screen(self.screen_name)

# The game starts here.
label start:
    # init needed data
    call init_all

    # plays the intro sequence
    call play_intro

    # enters the game proper
    call enter_game

    # plays the ending sequence
    call play_ending

    return

label init_all:
    default time_of_day = 2
    define config.window = Hide
    call init_locations
    return

label enter_game:
    $ bedroom.load_scene()