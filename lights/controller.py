import multiprocessing
from queue import Empty
from time import sleep
import json
import sys

from .patterns import pattern_library



SIM = True

""" 
At some point, I should maybe split this into two objects. One that just handles the lights and lives in the new process
and one that handles remembering the pid and stuff and has the routines for passing stuff through the queue.
"""

class LightController:
    def __init__(self, queue):
        self.state = {
            "pattern": "rainbow",
            "time": 0,
            "clock_tick_size": 0.01
        }
        self.queue = queue
        self.pattern_library = pattern_library

    def update_state(self, new_state):
        for key in new_state:
            self.state[key] = new_state[key]

    def setup_strip(self):
        with open('light-config.json') as config_file:
            config = json.load(config_file)

        # if config['simulation'] == True:
        if sys.platform == "darwin":
            from .simulator import Strip
            settings = config['simulation_settings']
            strip = Strip(settings['led_count'])
        else:
            from .neopixelWrapper import Strip
            settings = config['neopixel_settings']      # unfinished
            strip = Strip(**settings)
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
        strip = self.strip
        while True:
            active_pattern = self.pattern_library[self.state['pattern']]

            for pixel_index in range(strip.numPixels()):
                color = active_pattern.get_color(pixel_index, self.state['time'])
                strip.setPixelColor(pixel_index, color)
            strip.show()
            sleep(active_pattern.get_wait_time(self.state['time']))

            self.state['time'] = (self.state['time'] + self.state['clock_tick_size']) % 1
            self.check_queue()


def setup_and_run(queue):
    light_controller = LightController(queue)
    light_controller.setup_strip()
    light_controller.mainloop()