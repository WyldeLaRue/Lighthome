from . import neopixelWrapper
from . import patterns
from time import sleep


strip = neopixelWrapper.Strip(300)

time = 0
while True:
    active_pattern = patterns.RainbowCycle()

    for pixel_index in range(strip.numPixels()):
        color = active_pattern.get_color(pixel_index, time)
        strip.setPixelColor(pixel_index, color)
    strip.show()

    time += 0.01
    time = time % 1