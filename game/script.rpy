# Main script for the demo!

define n = Character("Nighten", image="nighten")

# NVL characters are used for the phone texting
define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Skip the main menu
label main_menu:
    return

label start:
    scene bg village with dissolve
    pause 1.0

    show nighten normal e1m1 at center:
        yoffset 1080
        ease 0.7 yoffset 0


    n "Hello! Welcome to this demo!"
    n e1m2 "I'm very proud to show you what I've been working on: a brand new phone system for Ren'Py!"
    n phone e1m1 "And to show you how it work, we have a special guest!"

    #Phone conversation start
    show nighten e1m2_b:
        ease 0.5 xalign 0.7 

    nvl_narrator "Nighten added Eileen to the group"
    n_nvl e2m2_b "Hey! Welcome to the demo Eileen!"
    e_nvl "who's this?"
    n_nvl e2m1_b "haha, silly you"
    n_nvl e1m2_b "We talked about showing off the phone the other day, remember?"
    e_nvl "it's today? {image=emoji/fear.png}"
    e_nvl "oops sorry night', I forgot {image=emoji/sweat.png}"
    n_nvl "No problem, you must be quite busy!"
    n_nvl e2m2_b "congrat on showing the emoji tho {image=emoji/clap.png}"
    e_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    n_nvl e1m2 "But since we use regular renpy, we can use the same principle to send pictures!"
    e_nvl "Right! Let me take a selfie {image=emoji/camera.png}"
    show nighten e1m2_b
    e_nvl "{image=EileenSelfieSmall.png}"
    n_nvl e2m1_b "awww, you look fantastic!"
    show nighten e2m2_b
    e_nvl "A bit low res but hey, the pic has to fit the screen somehow"
    
    n_nvl "Thank you Eileen for doing this demo with me!"
    e_nvl "no problem, I hope people will make good use of it!"
    e_nvl "byyee {image=emoji/wave.png}"


    show nighten:
        ease 0.5 xalign 0.5 

    n e1m2 "That's it for the demo!"
    n normal e1m2 "Do you have any question?"

    jump question

label question:
    menu:
        "What do you want to know?"
        "How is this phone working?":
            n e2m2 "To put it simply, it's just another style for the NVL mode."
            n e2m1 "Yep, it's not much more complicated than that!"
            n e1m1 "The main thing was to make it look like a phone, with a scrollable feed and the correct placement for the text."
            n e1m2 "Knowing that, you can probably build your own phone screen; but mine can still be used as a base if needed!"
            jump question


        "How to add it to my {i}*awesome*{/i} project?":
            n e1m2 "First, add PhoneTexting.rpy to your project directory. Don't forget to edit MC_Name to your main character name!"
            n e2m2 "Then you'll have to edit the nvl screen in screen.rpy, or else it's not gonna work!"
            n e1m2 "In gui.rpy, change gui.nvl_list_length to None, so that messages don't disapear."
            n e1m1 "And you now just have to create nvl characters and made them speak!"
            n e1m2 "If you want to use the regular NVL screen, change the nvl_mode variable to \"classic\", and back to \"phone\" if you want to use it again!"
            n e2m2 "Of course check the more detailed instruction on the project page, but that's all there is to it! You should have something somewhat functionnal at this point."
            jump question


        "Who made this?":
            n e1m1 "The code is created by me, Nighten!"
            n e1m2 "I also drew my sprite and the phone UI, using Krita, Rebelle 3 and Inkscape."
            n "All the source are available in the folder and on {a=https://github.com/NightenDushi}github{/a}, feel free to use it in your project."
            n e2m2 "Credits would be appreciated, but not mandatory!"
            n e1m2 "The background is created by our dear Uncle Mugen! You can find more of his work on {a=https://lemmasoft.renai.us/forums/viewtopic.php?t=17302}LemmaSoft{/a}!"
            jump question
        
        "Why {i}another{/i} phone/messaging system?":
            n e2m2 "Well, mostly because I found the other one available way too complicated, and not really friendly to use."
            n e1m1 "I wanted a system that feels like renpy, so that you can understand it and build on it."
            n e1m2 "And I think more option is great for the community in general!"
            n e2m1 "But I don't think this system is perfect, far from it!"
            jump question
            
        "Nothing, have a good day!":
            jump end

label end:
    n e2m2 "Aww, thank you! Most people just close the game without saying goodbye, so I appreciate it a lot!"
    n e1m2 "If you still have some questions, don't hesitate to message me on Discord {i}(Nighten#3081){/i}!"
    n e1m1 "And if you want further help, you can also hire me as a programmer! {a=https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647}All the details are here{/a}."
    n e2m1 "Take care! I wish you good things in life!"
    $ renpy.quit()