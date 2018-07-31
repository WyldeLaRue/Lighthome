import multiprocessing
from queue import Empty
from time import sleep
import json

from .controller import setup_and_run

class LightProcessManager:
    def __init__(self):
        self.queue = None
        self.pid = None
        self.process = None

    def create_process(self):
        self.queue = multiprocessing.Queue()
        self.process = multiprocessing.Process(target=setup_and_run, args=(self.queue,))

    def start(self):
        self.process.start()

    # This one gets called by the outside world.
    def change_state(self, new_state):
        self.queue.put(new_state)

light_process_manager = LightProcessManager()