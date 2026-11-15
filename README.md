
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

## Setup
1. Copy into your `game/` folder:
   - `PhoneTexting.rpy`
   - `images/phone_background.png`, `phone_foreground.png`, `phone_send_frame.png`, `phone_received_frame.png`, `phone_send_icon.png`, `phone_received_icon.png`
   - `audio/SendText.ogg`, `audio/ReceiveText.ogg` (only if you use the sound callbacks)
2. In `screens.rpy`, edit the `nvl` screen:
```renpy
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
3. In `gui.rpy`: `define gui.nvl_list_length = None` (keeps every message).
4. Set your MC's name in `PhoneTexting.rpy`: `default MC_Name = "Nighten"`.
5. Make `kind=nvl` characters speak:
```renpy
define n_nvl = Character("Nighten", kind=nvl, callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)
```
- Emojis and pictures: use an `{image=...}` tag, sized for the phone screen.
- To get the regular NVL screen back, set `nvl_mode` to anything else (e.g. `"classic"`).

## FAQ

**My MC's messages show on the wrong side / I use a player-entered name.**
`MC_Name` must match the displayed name. It can be a list, and `[player_name]`-style names work (substituted before comparing):
```renpy
default MC_Name = ["[player_name]", "Nighten"]
```
Or mark any character as the MC: `Character("[player_name]", kind=nvl, who_style="phone_mc")`.

**Dialogue appears in the normal textbox, not the phone.**
The character isn't an NVL character. Add `kind=nvl`.

**The phone disappears.**
Expected: the phone is the NVL screen, so it hides while a normal (ADV) character speaks. It comes back, with its history, on the next NVL line.

**Text is invisible or uses the wrong font.**
Your game's default text style is leaking in (e.g. white text on a white bubble). Set the phone styles explicitly (next question).

**How do I change fonts, colours, bubble width or background?**
Text styles: `phone_narrator_text`, `phone_name_text`, `phone_mc_text`, `phone_other_text`. Bubble styles: `phone_mc_bubble`, `phone_other_bubble`.
```renpy
style phone_mc_text:
    font "myfont.ttf"
    color "#fff"
style phone_other_bubble:
    background Frame("my_bubble.png", 23, 23)
    padding (20, 20)
    xsize 400
```
The phone itself is `phone_background.png` / `phone_foreground.png`: replace the images.

**Per-character avatars?**
Key by displayed name; anyone missing uses the default icon:
```renpy
define phone_icons = {"Eileen": "eileen_icon.png"}
```

**Choices inside the phone?**
Use `menu (nvl=True):`. A plain `menu:` shows the normal overlay choice. Style the buttons with `phone_choice_button` / `phone_choice_text`.

**How do I clear messages / have separate conversations?**
`nvl clear` empties the phone. For a separate history per contact:
```renpy
default phone_threads = {}
init python:
    def phone_open(name):
        store.nvl_list = store.phone_threads.setdefault(name, [])
```
Call `$ phone_open("Eileen")` before that conversation; call it again after any `nvl clear`.

**Which files do I copy?**
See [Setup](#setup) step 1. The `gui/phone/` folder is Ren'Py's own mobile GUI, not this phone.

[Mirror download on my website](https://nighten.fr/files/yet_another_phone/)

[Browser demo on *itch.io*](https://nighten.itch.io/yet-another-phone-renpy)

## Credits:
The background is made by [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302). All the other art assets are done by me, **Nighten**, and free to use in your project if you want (the sources file are available).

And if you need more help for your project, [you can hire me as a programmer!](https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647) :) ✨

Have a nice day!
