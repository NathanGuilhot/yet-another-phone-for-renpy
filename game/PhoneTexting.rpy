# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "Nighten" ##The name of the main character, used to place them on the screen

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    style "phone_narrator_text"
                    prefer_screen_to_id True
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == MC_Name:
                $ message_style = "phone_mc"
            else:
                $ message_style = "phone_other"

            hbox:
                spacing 10
                if d.who == MC_Name:
                    box_reverse True
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == MC_Name:
                        $ message_icon = "phone_send_icon.png"
                    else:
                        $ message_icon = "phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != MC_Name and previous_d_who != d.who:
                        text d.who style "phone_name_text"

                    frame:
                        style message_style + "_bubble"

                        if d.current:
                            if d.who == MC_Name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            style message_style + "_text"
                            prefer_screen_to_id True
                            slow_cps False
                            id d.what_id
        $ previous_d_who = d.who
                    
## Phone text and bubble styles: override these in your game to restyle the phone.
## They set font, size, color and outlines explicitly so the host game's
## default text style (and the nvl_dialogue style) doesn't leak in.
style phone_narrator_text is default:
    font "DejaVuSans.ttf"
    size 28
    color "#404040"
    outlines []
    italic True
    text_align 0.5
    xalign 0.5
    xmaximum 350

style phone_name_text is default:
    font "DejaVuSans.ttf"
    size 33
    color "#404040"
    outlines []

style phone_mc_text is default:
    font "DejaVuSans.ttf"
    size 33
    color "#fff"
    outlines []
    text_align 1.0
    xalign 1.0

style phone_other_text is default:
    font "DejaVuSans.ttf"
    size 33
    color "#000"
    outlines []
    text_align 0.0

style phone_mc_bubble is default:
    background Frame("phone_send_frame.png", 23, 23, 23, 23)
    padding (20, 20)
    xsize 350

style phone_other_bubble is default:
    background Frame("phone_received_frame.png", 23, 23, 23, 23)
    padding (20, 20)
    xsize 350

style phoneFrame is default

style phoneFrame_frame:
    background Transform("phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)
    
    ysize 815
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True


