# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define a = Character("Angela")
define d = Character("Derek") 
define j = Character("Jack")
define s = Character("Scarlett")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    "insert deep quote"

    scene bg bedroom 1

    
    show you neutral

    # These display lines of dialogue.

    "you wake up, rubbing the sleep out of your eyes."

    "another day of school."

    "tomorrow is your first day as the student council secretary."

    "are you ready?"

    menu:
        "yes":
            "you have been ready for this day since the moment you entered the high school."
            "you have always worked for something greater than yourself, haven't you?"
        "no":
            "you have worked for this day for years."
            "how can you ever feel fully ready to take on these new responsibilities?"
    
    "time to get ready."

    menu: 
        "go to bathroom"

    scene bg mirror 1

    "you look at yourself in the mirror."

    "..."

    "you aren't looking too bad today, huh?"



    return
