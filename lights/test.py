from neopixelWrapper import Strip
from time import sleep
import patterns


strip = Strip(led_count=300, led_pin=18, led_freq_hz=800000, led_dma=5, led_brightness=255, led_invert=False, led_channel=0)

time = 0
active_pattern = patterns.RainbowCycle()
while True:

    for pixel_index in range(strip.numPixels()):
        color = active_pattern.get_color(pixel_index, time)
        strip.setPixelColor(pixel_index, color)
    strip.show()
    sleep(0.01)
    time += 0.01
    time = time % 1
