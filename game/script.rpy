# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define a = Character("Angela")
define d = Character("Derek") 
define j = Character("Jack")
define s = Character("Scarlett")


#functions

init python:
    def increment():
        for i in range(0,3):
            count = 0
            if count == 0:
                idle image
                $ count++
            elif count == 1:
                idle image
                $ count++
            elif count == 2:
                idle image
                $ count++
            else:
                action Hide("eating")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
 
    "insert deep quote"

    scene bg bedroom 1
    with fade
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
            "how can you ever feel fully prepared to take on these new responsibilities?"
    
    "time to get ready."

    scene bg kitchen 1
    with fade
    
    "a good day always starts with a full and healthy breakfast."

    "will you eat breakfast?"

    menu:
        "yes":
            "you decide to take the extra minute to eat breakfast."
            window hide
            screen eating():
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    action Function(increment)
                    
            show screen eating
                    

                    


        "no":
            "today, you think you're too good for a nice breakfast."
            "you decide to skip. you have to make as much time as you can for the other stuff, right?"
            

    scene bg mirror 1
    with fade

    "you look at yourself in the mirror."

    "..."

    "you aren't looking too bad today, huh?"

    "you are ready."

    scene bg hallway 1 
    with fade 



    return
