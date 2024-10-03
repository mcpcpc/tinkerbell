# Tinkerbell
An experiment in Christmas tree lighting to create a "pixie dust" effect using multiple NeoPixel strands.

## Materials
* [Soft Flexible Wire NeoPixel Strand](https://www.adafruit.com/product/4560) - Qty 8
* [3-pin JST SM Plug](https://www.adafruit.com/product/1663) - Qty 8
* [Adafruit Feather RP2040 SCORPIO](https://www.adafruit.com/product/5650) - Qty 1
* [Machine-Mount Corrosion-Resistant Washdown Enclosure](https://www.mcmaster.com/product/1037N112) - Qty 1
* [5V 4A Switching Power Supply](https://www.adafruit.com/product/1466) - Qty 1
* [M3 Thread 4mm Long Thread Forming Phillips Screws](https://www.mcmaster.com/product/94209A353) - Qty 4
* [Tinkerbell PCA](bin/tinkerbell_r1.zip) - Qty 1

## Assembly
### Software
The following are high-level steps to get the microcontroller up and running:

1. Download and install the latest version of CircuitPython ([here](https://circuitpython.org/board/adafruit_feather_rp2040_scorpio/)) to the Adafruit Feather RP2040 SCORPIO.
2. Download abd unpack/unzip the latest CircuitPython library bundle ([here](https://circuitpython.org/libraries)). From the unpacked directory, copy the `adafruit_led_animation/` folder and `neopixel.mpy` file to the `lib/` folder of the *CIRCUITPY* drive.
3. Copy and/or replace the `code.py` on the *CIRCUITPY* drive with the one from this repository.

## References
* https://learn.adafruit.com/introducing-feather-rp2040-scorpio?view=all
* https://learn.adafruit.com/circuitpython-led-animations/basic-animations
 