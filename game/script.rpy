# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define a = Character("Angela")
define d = Character("Derek") 
define j = Character("Jack")
define s = Character("Scarlett")


#functions



#screens


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
                    
            

            screen eat1():
                modal True
                imagebutton:
                    align (0.5, 0.5)

                    idle "test1.png"

                    action Return()
            call screen eat1

            screen eat2():
                modal True
                imagebutton:
                    align (0.5, 0.5) 

                    idle "test2.webp"

                    action Return() 
            call screen eat2

            screen eat3(): 
                modal True
                imagebutton:
                    align (0.5, 0.5)

                    idle "test3.webp"
                    
                    action Return()
            call screen eat3
            pause 1.0

            "you finished your breakfast."
            "time to go the bathroom."


        "no":
            "today, you think you're too good for a nice breakfast."
            "you decide to skip. you have to make as much time as you can for the other stuff, right?"
            "you have to go to the bathroom."

    scene bg mirror 1
    with fade

    "you look at yourself in the mirror."

    "..."

    "you aren't looking too bad today, huh?"

    "you are ready."

    scene bg hallway 1 
    with fade

    "you arrive at the school. a familiar scene greets you." 

    a "BOO!" with hpunch
    
    you "jesus christ angela..."

    "you sigh. she knows you get scared easily."

    a "sorry... you know I can't help it!"

    #add a bunch of dialogue everywhere, this just an outline

    scene bg history
    with fade

    scene bg math
    with fade

    scene bg free_period
    with fade

    scene bg english
    with fade

    "finally, you arrive at english. it has always been your favorite class."
    "you used to stay up all night reading books, and the books from english class were never any different."
    "most books that you read in this class have some sort of meaning to you. each one has changed your perspective, even just a little bit."
    "and, of course, it helps that angela is in your class this year as well."

    a "hey! did you finish the reading today?"

    you "I-"

    "angela scoffs."

    a "of course you did, what am I saying?"

    "before you can try to respond, she cuts you off again."

    a "sorry, how was your day?"

    you "it actually wasn't too bad today. I met some of the other student council members."

    a "really? what do you think??"

    you "well..."

    "you try to begin again, but the teacher's voice cuts you off. class is starting."

    a "hey, do you want to talk about this after school? we can go get dumplings!"

    you "I..."

    menu:
        "go with angela":
            "the others offered to hang out after school, but angela is and has always been your best friend after all."
            you "sounds good!"

            jump angela_path
        "go with derek":
            "something about the way derek looked at you, the way he talked to you makes you want him to keep looking at you and talking to you."
            you "sorry, I actually already agreed to watch derek's baseball game after school!"

            a "who's jack?"

            "the teacher calls you and angela out, silencing you for the rest of the class."
        "go with jack":
            "you wonder how it would be like to hang out with someone who worked as hard as you did. maybe jack would be a better option today."
            you "I'm actually going to go to the cafe with jack after school today, sorry!"

            a "who's jack?"

            "the teacher calls you and angela out, silencing you for the rest of the class."

            jump derek_path
        "go with scarlett":
            "earlier today, scarlett seemed to have some sort of glow to her. she listened to your every word. you want to see more of her."
            you "sorry, I already agreed to go to the vinyl store with scarlett after school today!"

            a "who's scarlett?"

            "the teacher calls you and angela out, silencing you for the rest of the class."

            jump scarlett_path
        "go home.":
            "you're too tired for this."
            you "sorry, I want just want to go home."

            a "oh, okay. text me later!"

            you "sure." 

            jump alone_path

label angela_path:
    scene bg dumpling
    with fade

    "you go with angela to get dumplings."

label derek_path:
    scene bg baseball
    with fade

label jack_path:
    scene bg cafe
    with fade

label scarlett_path:
    scene bg vinyl
    with fade

label alone_path:
    scene bg desk 
    with fade
    
    "you went home after school and did all of your homework."
    "but now you're still here, studying."
    "you have so much to do..."


    

    return
