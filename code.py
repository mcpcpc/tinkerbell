#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SPDX-FileCopyrightText: 2024 Michael Czigler
SPDX-License-Identifier: BSD-3-Clause

Tinkerbell NeoPixel animation effect.
"""

from random import randint

from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.color import GOLD
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
from neopixel import GRBW

LOCALE = [
    (NEOPIXEL0, 50),
    (NEOPIXEL1, 50),
    (NEOPIXEL2, 50),
    (NEOPIXEL3, 50),
    (NEOPIXEL4, 50),
    (NEOPIXEL5, 50),
    (NEOPIXEL6, 50),
    (NEOPIXEL7, 50),
]
#RGB = (32, 200, 32)
RGB = GOLD


def get_pixels(pin, n: int):
    """
    Create and return NeoPixel object.
    """

    return NeoPixel(
        pin,
        n,
        brightness=0.5,
        auto_write=False,
        pixel_order=GRBW,
    )


def get_comet(pixels: NeoPixel, color: tuple):
    """
    Create and return Comet object.
    """

    speed = randint(50, 100) / 100
    length = randint(3, 7)
    return Comet(
        pixels,
        speed=speed,
        color=color,
        tail_length=length,
        reverse=True,
    )


def main():
    pixels = list(map(lambda l: get_pixels(*l), LOCALE))
    comet_effects = list(map(lambda p: get_comet(p, RGB), pixels))
    comet_group = AnimationGroup(*comet_effects, sync=False)
    sequence = AnimationSequence(comet_group)
    while True:
        sequence.animate()


if __name__ == "__main__":
    main()
