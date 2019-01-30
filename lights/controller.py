import multiprocessing
from queue import Empty
from time import sleep
import json
import sys

from .patterns import pattern_library
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




class LightController:
    def __init__(self, queue):
        self.state = {
            "pattern": "rainbow",
            "clock_time": 0,
            "clock_tick_size": 0.01,
            "brightness": 0.5
        }
        self.queue = queue
        self.pattern_library = pattern_library

    def update_state(self, new_state):
        for key in new_state:
            self.state[key] = new_state[key]

    def setup_strip(self):
        self.SIM=False
        return
        with open('light-config.json') as config_file:
            config = json.load(config_file)

        # if config['simulation'] == True:
        if sys.platform == "darwin":
            from .simulator import Strip
            settings = config['simulation_settings']
            strip = Strip(settings['led_count'])
            self.SIM = True
        else:
            from .neopixelWrapper import Strip
            settings = config['neopixel_settings']      # unfinished
            strip = Strip(**settings)
            self.SIM = False
        self.strip = strip

    def check_queue(self):
        received_data = None
        while not self.queue.empty():
            try:
                received_data = self.queue.get_nowait()
            except Empty:
                received_data = None

        if received_data is not None:
            self.update_state(received_data)
    
    def mainloop(self):
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        strip.begin()
        while True:
            active_pattern = self.pattern_library[self.state['pattern']]
            time = self.state['clock_time']

            for pixel_index in range(strip.numPixels()):
                color = active_pattern.get_color(pixel_index, time, **self.state)
                if not self.SIM:
                    color.voltageOffset(pixel_index)
                    color.setBrightness(self.state['brightness'])
                
                strip.setPixelColor(pixel_index, Color(color.red, color.blue, color.green, color.white))
            strip.show()
            wait_ms = active_pattern.get_wait_time(self.state['clock_time'])
            sleep(wait_ms/1000.0)

            self.state['clock_time'] = (self.state['clock_time'] + self.state['clock_tick_size']) % 1
            self.check_queue()


def setup_and_run(queue):
    light_controller = LightController(queue)
    light_controller.setup_strip()
    light_controller.mainloop()
