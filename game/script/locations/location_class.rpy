init python:
    class location:
        # constructor called upon initialization of object
        def __init__(self, name, bg_day, bg_evening, bg_night):
            self.name = name
            # self.screen_name = screen_name
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

        # load the location
        def load(self):
            renpy.scene()
            renpy.show(self.get_current_bg())
            renpy.call_screen(self.name)

label init_locations:
    default bedroom = location("bedroom", "bedroom_day", "bedroom_evening", "bedroom_night")
    default livingroom = location("livingroom", "livingroom_day", "livingroom_day", "livingroom_night")
    # default kitchen = location("kitchen", "kitchen", "livingroom_day", "livingroom_day", "livingroom_night")
