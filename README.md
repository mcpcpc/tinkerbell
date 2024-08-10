# Tinkerbell

![Tinker Bell](https://upload.wikimedia.org/wikipedia/commons/4/42/Tinkclose-1-.jpg)

An experiment in Christmas tree lighting to recreate a "pixie dust" effect using multiple NeoPixel strands.

## Materials

* [Adafruit Soft Flexible Wire NeoPixel Strand](https://www.adafruit.com/product/4560) (Qty 8)
* [3-pin JST SM Plug](https://www.adafruit.com/product/1663) (Qty 8)
* [Adafruit Feather RP2040 SCORPIO](https://www.adafruit.com/product/5650) (Qty 1)

## Setup
The following are high-level steps to get the microcontroller up and running:

1. Download and install the latest version of CircuitPython ([here](https://circuitpython.org/board/adafruit_feather_rp2040_scorpio/)) to the Adafruit Feather RP2040 SCORPIO.
2. Download abd unpack/unzip the latest CircuitPython library bundle ([here](https://circuitpython.org/libraries)). From the unpacked directory, copy the `adafruit_led_animation/` folder and `neopixel.mpy` file to the `lib/` folder of the *CIRCUITPY* drive.
3. Copy and/or replace the `code.py` on the *CIRCUITPY* drive with the one from this repository.

## References
* https://learn.adafruit.com/introducing-feather-rp2040-scorpio?view=all
* https://learn.adafruit.com/circuitpython-led-animations/basic-animations
 