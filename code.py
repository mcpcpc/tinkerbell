#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SPDX-FileCopyrightText: 2024 Michael Czigler
SPDX-License-Identifier: BSD-3-Clause

Tinkerbell NeoPixel animation effect.
"""

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
from random import random
from random import randint

PER_STRAND_N = const(3)
PIXELS = [
    NEOPIXEL0,
    NEOPIXEL1,
    NEOPIXEL2,
    NEOPIXEL3,
    NEOPIXEL4,
    NEOPIXEL5,
    NEOPIXEL6,
    NEOPIXEL7,
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


def get_pixels(pin):
    """
    Create and return NeoPixel object.
    """

    return NeoPixel(
        pin,
        PER_STRAND_N,
        brightness=0.2,
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
        #speed=0.01,
        speed=speed,
        color=RED,
        #tail_length=5,
        tail_length=length,
        reverse=True,
        ring=True,
    )


def main():
    pixels = list(map(get_pixels, PIXELS))
    effects = list(map(get_comet, pixels))
    group = get_animation_group(*effects)
    sequence = get_animation_sequence(group)
    while True:
        sequence.animate()


if __name__ == "__main__":
    main()
