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

    "You wake up, rubbing the sleep out of your eyes."

    "Another day of school."

    "Tomorrow is your first day as the student council secretary."

    "Are you ready?"

    menu:
        "Yes":
            "You have been ready for this day since the moment you entered the high school."
            "You have always worked for something greater than yourself, haven't you?"
        "No":
            "You have worked for this day for years."
            "How can you ever feel fully prepared to take on these new responsibilities?"
    
    "Time to get ready."

    scene bg kitchen 1
    with fade
    
    "A good day always starts with a full and healthy breakfast."

    "Will you eat breakfast?"

    menu:
        "Yes":
            "You decide to take the extra minute to eat breakfast."
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

            "You finished your breakfast."
            "Time to go the bathroom."


        "No":
            "Today, you think you're too good for a nice breakfast."
            "You decide to skip. you have to make as much time as you can for the other stuff, right?"
            "You have to go to the bathroom."

    scene bg mirror 1
    with fade

    "You look at yourself in the mirror."

    "..."

    "You aren't looking too bad today, huh?"

    "You are ready."

    scene bg hallway 1 
    with fade

    "You arrive at the school. A familiar scene greets you." 

    a "BOO!" with hpunch
    
    you "Jesus christ Angela..."

    "You sigh. She knows you get scared easily."

    a "Sorry... you know I can't help it!"

    #add a bunch of dialogue everywhere, this just an outline

    scene bg history
    with fade

    scene bg math
    with fade

    scene bg free_period
    with fade

    scene bg english
    with fade

    "Finally, you arrive at english. It has always been your favorite class."
    "You used to stay up all night reading books, and the books from english class were never any different."
    "Most books that you read in this class have some sort of meaning to you. Each one has changed your perspective, even just a little bit."
    "And, of course, it helps that Angela is in your class this year as well."

    a "Hey! Did you finish the reading today?"

    you "I-"

    "Angela scoffs."

    a "Of course you did, what am I even saying?"

    "Before you can try to respond, she cuts you off again."

    a "Sorry, how was your day?"

    you "It actually wasn't too bad. I met some of the other student council members."

    a "Really? What do you think??"

    you "Well..."

    "You try to begin again, but the teacher's voice cuts you off. Class is starting."

    a "Hey, do you want to talk about this after school? We can go get dumplings!"

    you "I..."

    menu:
        "Go with Angela":
            "The others offered to hang out after school, but Angela is and has always been your best friend."
            you "Sounds good!"

            jump angela_path
        "Go with Derek":
            "Something about the way Derek looked at you, the way he talked to you makes you want him to keep looking at you and talking to you."
            you "Sorry, I actually already agreed to watch Derek's baseball game after school!"

            a "Who's Derek?"

            "The teacher calls you and Angela out, silencing you for the rest of the class."
        "Go with Jack":
            "You wonder how it would be like to hang out with someone who works as hard as you did. Maybe jack would be a better option today."
            you "I'm actually going to go to the cafe with Jack after school today, sorry!"
 
            a "Who's Jack?"

            "The teacher calls you and Angela out, silencing you for the rest of the class."

            jump derek_path
        "Go with Scarlett":
            "Earlier today, Scarlett seemed to have some sort of glow to her. She listened to your every word. You want to see more of her."
            you "Sorry, I already agreed to go to the vinyl store with Scarlett after school today!"

            a "Who's Scarlett?"

            "The teacher calls you and Angela out, silencing you for the rest of the class."

            jump scarlett_path
        "Go home.":
            "You're too tired for this."
            you "Sorry, I want just want to go home."

            a "Oh, okay. Text me later!"

            you "Sure." 

            jump alone_path

label angela_path:
    scene bg dumpling
    with fade

    "You go with Angela to get dumplings."

    "You chat while you wait for your food to arrive."

    a "Okay, so! Tell me: What's with the other student council members?"

label derek_path:
    scene bg baseball
    with fade

    "You go to Derek's baseball game after school." 
    "With the sun warming your skin and the unintelligble chatter filling your ears, you allow yourself to relax for a moment."
    "You see the players on the field, and you spot Derek among them."
    "When he makes a home run, he spots you and waves."



    jump derek_path_2

label derek_path_2:

label jack_path:
    scene bg cafe
    with fade

    "You go to the cafe after school."
    "You see Jack waiting for you, his back facing you. He already has a coffee resting on the table."



    "The next day."

    jump jack_path_2

label jack_path_2:


label scarlett_path:
    scene bg vinyl
    with fade

    "You arrive at the vinyl store after school." 
    "The soft sound of music fills your ears as you open the door, a soft bell tinkling."
    "The smiling face of Scarlett greets you as you scan the store."





    "The next day."


    jump scarlett_path_2

label scarlett_path_2:



label alone_path:
    scene bg desk 
    with fade
    
    "You went home after school and did all of your homework."
    "But you're still here, hours later, studying."
    "You have so much to do..."
    "You can't stop to relax."
    
    jump alone_path_2

label alone_path_2:




    return
