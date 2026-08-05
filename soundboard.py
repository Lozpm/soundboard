import pygame
from gpiozero import Button
from signal import pause

pygame.mixer.init()

SOUND_DIR = "/home/loz/soundboard/"

sounds = {
    "air_horn": pygame.mixer.Sound(SOUND_DIR + "air_horn.wav"),
    "air_raid": pygame.mixer.Sound(SOUND_DIR + "air_raid.wav"),
    "blam": pygame.mixer.Sound(SOUND_DIR + "blam.wav"),
    "boom": pygame.mixer.Sound(SOUND_DIR + "boom.wav"),
    "bruh": pygame.mixer.Sound(SOUND_DIR + "bruh.wav"),
    "dub_siren": pygame.mixer.Sound(SOUND_DIR + "dub_siren.wav"),
    "gun_shot": pygame.mixer.Sound(SOUND_DIR + "gun_shot.wav"),
    "wah_wah": pygame.mixer.Sound(SOUND_DIR + "wah_wah_trombone.wav"),
}

# Map each sound name to the GPIO pin its button is wired to.
# Change these numbers to match your actual wiring.
pin_map = {
    "air_horn": 2,
    "air_raid": 3,
    "blam": 4,
    "boom": 17,
    "bruh": 27,
    "dub_siren": 22,
    "gun_shot": 10,
    "wah_wah": 9,
}

buttons = {}

for name, pin in pin_map.items():
    btn = Button(pin, pull_up=True, bounce_time=0.05)  # 50ms debounce
    # default-arg trick avoids the classic late-binding closure bug
    btn.when_pressed = lambda sound=sounds[name]: sound.play()
    buttons[name] = btn

print("Soundboard ready. Press Ctrl+C to quit.")
pause()  # sleeps efficiently, waiting for button events
