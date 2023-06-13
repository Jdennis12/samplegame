# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Jay = Character("Jay", color ="#01ff6b")
define Oak = Character("Professor Oak", color ="#e07715")
image pic1 = im.Scale("couch.jpg", 2560, 1440)
image pic2 = im.Scale("2v3.png", 2560, 1440)
image pic3 = im.Scale("pf.jpg", 2560, 1440)

# The game starts here.

label start:
    scene bg pic1
    show pic1
    "Welcome to my demo...."
    show dog at right
    Jay " \"W...Who are you?!\""
    show kakashi at truecenter
    Oak " \"My name is Professor Oak and I will teach you about the world of Pokemon!\""
    Jay "\"Awesome!\""   


label sprites:
    show pic2
    show dog at right
    Jay "Wow your back must hurt!"
    show k2 at left
    Oak "Not as bad as theres"

label character:
    Oak " \"Wow this sure is boring!\""
    Jay "Indeed!"

label background:
    Jay "\"Let's go to the gym!\""
    hide dog
    hide k2
    hide pic2
    show pic3
    with fade
    show kakashi 1 at center
    show dog at right

    
label bgm:
    play music "Gunna - Elevator.mp3" fadein 1.0 volume 0.01
    Jay "\"I love this song\""

label sfx:
    play sound "cm.mp3" volume .005
    show kakashi at left
    Oak "\"That sounds terrible!\"" 

label choices:
    default learned = False
    Jay "Do you want to do push ups or sit ups?"
menu:
    "Push ups":
        #block of code to run
        jump choices1_a

    "Sit ups":
        #block of code to run
        jump choices1_b

label choices1_a:
    Jay "Push ups it is!"
    $ learned = True
    jump choices1_common
label choices1_b:
    Jay "Abs on fire!"
    jump choices1_common

label choices1_common:
    Jay "..."
    Jay "end."

label flags:
    if learned: 
        Jay "Lets go!"
    else:
        Jay "Nope! "

label variables:
    $ PlayerScore = 0
    $ PlayerName = "Player"

    return
