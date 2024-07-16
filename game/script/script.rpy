# The script of the game goes in this file.
default time_of_day = 1
image   bg bedroom = "bedroom_night.png"

init python:
    class scene:
        # constructor called upon initialization of object
        def __init__(self, scene_name, screen_name, bg_day, bg_evening, bg_night):
            self.scene_name = scene_name
            self.screen_name = screen_name
            self.bg_day = bg_day
            self.bg_evening = bg_evening
            self.bg_night = bg_night

        def load(self):
            # select relevant bg according to time of day
            if time_of_day == 1:
                bg = self.bg_day
            elif time_of_day == 2:
                bg = self.bg_evening
            else:
                bg = self.bg_night
            
            # load scene
            renpy.scene("bg bedrooom_day") #
            renpy.call_screen(self.screen_name)

init:
    $ bedroom_object = scene("bedroom", "bedroom", "bg bedroom_day.png", "bg bedroom_evening.png", "bg bedroom_night.png")

# The game starts here.
label start:
    call init_all
    call play_intro
    call enter_game
    call play_ending
    return

label init_all:
    scene bg bedroom
    "test"
    return

label enter_game:
    $ bedroom_object.load()
    # scene bg bedroom_day
    # call screen bedroom