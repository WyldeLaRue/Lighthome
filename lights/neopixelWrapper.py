import time
import colorsys
from . import shared
import neopixel
import math
import random


LED_COUNT      = 300       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW   



# Wrapper that goes around the Adafruit_NeoPixel class
class Strip:
    def __init__(self, **kwargs):
        self.neopixel_strip = neopixel.Adafruit_NeoPixel(led_count, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        
    def setPixelColor(self, index, color):
        neopixel_color = neopixel.Color(color.green, color.red, color.blue, color.white)
        self.neopixel_strip.setPixelColor(index, neopixel_color)

    def show(self):
        self.neopixel_strip.show()

    def numPixels(self):
        return self.neopixel_strip.numPixels()

    def begin(self):    # This is just to match the syntax of the neopixel library
        pass    