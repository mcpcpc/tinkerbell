#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SPDX-FileCopyrightText: 2024 Michael Czigler
SPDX-License-Identifier: BSD-3-Clause

Tinkerbell NeoPixel animation effect.
"""

from random import random
from random import randint

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

PIXELS = [
    (NEOPIXEL0, 50),
    (NEOPIXEL1, 50),
    (NEOPIXEL2, 50),
    (NEOPIXEL3, 50),
    (NEOPIXEL4, 50),
    (NEOPIXEL5, 50),
    (NEOPIXEL6, 50),
    (NEOPIXEL7, 50),
]


def get_animation_group(*args):
    """
    Create and return animation group.
    """

    return AnimationGroup(*args, sync=False)


def get_animation_sequence(*members):
    """
    Create and return animation sequence.
    """

    return AnimationSequence(*members)


def get_pixels(pin, n):
    """
    Create and return NeoPixel object.
    """

    return NeoPixel(
        pin,
        n,
        brightness=0.5,
        auto_write=False,
    )


def get_comet(pixels: NeoPixel):
    """
    Create and return Comet object.
    """

    speed = random()
    length = randint(3, 7)
    return Comet(
        pixels,
        speed=speed,
        color=RED,
        tail_length=length,
        reverse=True,
    )


def main():
    pixels = list(map(lambda p; get_pixels(*p), PIXELS))
    effects = list(map(get_comet, pixels))
    group = get_animation_group(*effects)
    sequence = get_animation_sequence(group)
    while True:
        sequence.animate()


if __name__ == "__main__":
    main()
