# The script of the game goes in this file.
default time_of_day = 2
default test = ""

label clear_scene:
    scene
    return


init python:
    class location:
        # constructor called upon initialization of object
        def __init__(self, scene_name, screen_name, bg_day, bg_evening, bg_night):
            self.scene_name = scene_name
            self.screen_name = screen_name
            self.bg_day = bg_day
            self.bg_evening = bg_evening
            self.bg_night = bg_night

        # returns the correct bg according to time of day
        def get_current_bg(self):
            if time_of_day == 1:
                bg = self.bg_day
            elif time_of_day == 2:
                bg = self.bg_evening
            else:
                bg = self.bg_night
            return bg

        def load(self):
            back = self.get_current_bg
            renpy.scene()
            renpy.show("bg_day")

        # def load(self):
        #     # select relevant bg according to time of day
        #     if time_of_day == 1:
        #         bg = self.bg_day
        #     elif time_of_day == 2:
        #         bg = self.bg_evening
        #     else:
        #         bg = self.bg_night
            
        #     # load background
        #     renpy.call("clear_scene", from_current=False)
        #     renpy.return_statement()
        #     renpy.scene()
        #     renpy.show(bg)

        #     # load interactibles
        #     renpy.call_screen(self.screen_name)

init:
    $ bedroom_object = location("bedroom", "bedroom", "bg_day", "bg_evening", "bg_night")

# The game starts here.
label start:
    # call init_all
    call play_intro
    call enter_game
    call play_ending
    return

# label init_all:
#     return

label enter_game:
    call load_scene(bedroom_object)
    # $ bedroom_object.load()
    # call load_scene(bedroom_object)

    # fades out the text box and then changes the bg
    # scene bg_day
    # call screen bedroom

    # # fades out the text box and then changes the bg
    # scene bg_day
    # $ renpy.call_screen("bedroom")

    # # changes the bg and then fades out the box
    # $ renpy.scene()
    # $ renpy.show("bg_day")
    # call screen bedroom

    # changes the bg and keeps the text box on screen, no fade
    # $ renpy.scene()
    # $ renpy.show("bg_day")
    # $ renpy.call_screen("bedroom")

    # jank solution
    # scene
    # $ renpy.show("bg_day")
    # $ renpy.call_screen("bedroom")

label load_scene(bedroom_object):
    $ bg = bedroom_object.get_current_bg()
    scene expression bg