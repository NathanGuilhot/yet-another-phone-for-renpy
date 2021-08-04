
![demo](https://nighten.fr/wp-content/uploads/2021/08/demo_phone_renpy.webp)

```renpy
# How this scene is implemented:

nvl_narrator "Nighten added Eileen to the group"
n_nvl e2m2 "Hey! Welcome to the demo Eileen!"
e_nvl "who's this?"
n_nvl e2m1 "haha, silly you"
n_nvl e1m2 "We talked about showing off the phone the other day, remember?"
e_nvl "it's today? {image=emoji/fear.png}"
```

# yet another phone for Ren'Py
 a simple phone UI/script for renpy, with a focus on ease of use :)

## Instructions:
- Add PhoneTexting.rpy to your project folder
- Edit the nvl screen in screen.rpy as follow:
```python
screen nvl(dialogue, items=None):

    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
    ####
        ## Indent the rest of the screen
        window:
            style "nvl_window"
            # ...
```
- Change gui.nvl_list_length in gui.rpy to None, so that all the message are shown 
- You'll then have to make a nvl character speak!
- To use the regular nvl screen again, change the nvl_mode variable to something else, like "classic"
- To include emojis and pictures, you can simply add use an image tag; make sure they are the right size for the phone screen.

[Mirror download on my website](https://nighten.fr/files/yet_another_phone/)

[Browser demo on *itch.io*](https://nighten.itch.io/yet-another-phone-renpy)

## Credits:
The background is made by [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302). All the other art assets are done by me, **Nighten**, and free to use in your project if you want (the sources file are available).

And if you need more help for your project, [you can hire me as a programmer!](https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647) :) ✨

Have a nice day!
