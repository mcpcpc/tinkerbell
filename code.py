#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SPDX-FileCopyrightText: 2024 Michael Czigler
SPDX-License-Identifier: BSD-3-Clause

Tinkerbell NeoPixel animation effect.
"""

from random import randint

from adafruit_led_animation.animation.comet import Comet
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
from neopixel import RGB

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
COLOR = (255, 80, 0)


def get_pixels(pin, n: int):
    """
    Create and return NeoPixel object.
    """

    return NeoPixel(
        pin,
        n,
        brightness=0.5,
        auto_write=False,
        pixel_order=RGB,
    )


def get_comet(pixels: NeoPixel, color: tuple):
    """
    Create and return Comet object.
    """

    speed = randint(15, 25) / 100
    length = randint(3, 7)
    return Comet(
        pixels,
        speed=speed,
        color=color,
        tail_length=length,
        reverse=True,
    )


def main(color: tuple = COLOR, locale: list = LOCALE):
    pixels = list(map(lambda l: get_pixels(*l), locale))
    comets = list(map(lambda p: get_comet(p, color), pixels))
    group = AnimationGroup(*comets, sync=False)
    sequence = AnimationSequence(group)
    try:
        print("starting...")
        while True:
            sequence.animate()
    except KeyboardInterrupt:
        print("cleanup...")
        list(map(lambda p: p.deinit(), pixels))


if __name__ == "__main__":
    main()
