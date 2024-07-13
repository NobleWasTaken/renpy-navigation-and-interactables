label play_ending:
    scene bg shrine_night
    "This is the game's ending scene."
    "It plays only once, when the game reaches the end of the script."
    "Usually, players should not be able to get to this point as the main game game loop would need to have returned for that to be possible."
    "Once it returns, the game will return to the main menu."
    return