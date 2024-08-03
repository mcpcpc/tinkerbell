from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.color import RED
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from board import NEOPIXEL0
from board import NEOPIXEL1
from board import NEOPIXEL2
from board import NEOPIXEL3
from board import NEOPIXEL4
from board import NEOPIXEL5
from board import NEOPIXEL6
from board import NEOPIXEL7
from neopixel import NeoPixel


def get_pixels(pin):
    return NeoPixel(
        pin,
        3,
        brightness=0.2,
        auto_write=False,
    )


def get_comet(pixels: NeoPixel):
    return Comet(
        pixels,
        speed=0.01,
        color=RED,
        tail_length=10,
        bounce=True,
    )


def main():
    pixels0 = get_pixels(NEOPIXEL0)
    comet0 = get_comet(pixels0)
    while True:
        comet.animate()


if __name__ == "__main__":
    main()
