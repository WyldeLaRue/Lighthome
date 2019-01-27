from time import sleep
import patterns
from neopixel import * 

LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
#LED_STRIP      = ws.SK6812_STRIP_RGBW
LED_STRIP      = ws.SK6812W_STRIP


#strip = Strip(led_count=300, led_pin=18, led_freq_hz=800000, led_dma=5, led_brightness=255, led_invert=False, led_channel=0)
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

time = 0
active_pattern = patterns.RainbowCycle()
while True:
    for pixel_index in range(strip.numPixels()):
        color = active_pattern.get_color(pixel_index, time)
        strip.setPixelColor(pixel_index, Color(color.red, color.blue, color.green, color.white))
    strip.show()
    sleep(0.02)
    time += 0.01
    time = time % 1
