from neopixelWrapper import Strip
from time import sleep
import patterns


strip = Strip(led_count=300, led_pin=18, led_freq_hz=800000, led_dma=5, led_brightness=255, led_invert=False, led_channel=0)

time = 0
while True:
    active_pattern = patterns.RainbowCycle()

    for pixel_index in range(strip.numPixels()):
        color = active_pattern.get_color(pixel_index, time)
        strip.setPixelColor(pixel_index, color)
    strip.show()
    sleep(active_pattern.get_wait_time(time)/1000.0)
    time += 0.01
    time = time % 1
