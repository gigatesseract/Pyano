import pyglet
from pyglet.window import key
import wav_util as wu
import os


def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return


notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.62,
    "F": 349.22,
    "G": 391.99,
    "A": 440.00,
    "B": 493.88,
    "C2": 523.25,
    "A#": 466.16,
}

seconds = 0.5
framerate = 44100.0
if not os.path.exists("sounds/"):
    os.makedirs("sounds/")

for key, value in notes.items():
    wu.create_sound(
        value, int(framerate * seconds), "sounds/" + key + ".wav", framerate
    )

key_bindings = {
    "z": "C",
    "x": "D",
    "c": "E",
    "v": "F",
    "b": "G",
    "n": "A",
    "m": "B",
    ",": "C2",
    "j": "A#",
}


window = pyglet.window.Window(width=100, height=100)


note = "hi"


@window.event
def on_draw():
    window.clear()
    label = pyglet.text.Label(
        note,
        font_name="Times New Roman",
        font_size=36,
        x=window.width // 2,
        y=window.height // 2,
        anchor_x="center",
        anchor_y="center",
    )
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    for key, value in key_bindings.items():
        if chr(symbol) == key:
            global note
            note = value

            # wu.play_sound(value + ".wav", True)
            sound = pyglet.resource.media("sounds/" + value + ".wav", streaming=False)
            sound.play()


pyglet.app.run()

