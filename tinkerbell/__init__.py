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

FAIRY_LIGHT_N = const(100)


def get_animation_group(*args):
    return AnimationGroup(*args, sync=False)


def get_animation_sequence(*members):
    return AnimationSequence(*members)


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
    effect0 = get_comet(pixels0)
    group0 = get_animation_group(effect0)
    sequence = get_animation_sequence(group0)
    while True:
        sequence.animate()


if __name__ == "__main__":
    main()
