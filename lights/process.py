import multiprocessing
from time import sleep

from .patterns import pattern_library

def main():
    pipe_out, pipe_in = multiprocessing.Pipe(False)
    light_controller = multiprocessing.Process(target=light_process_mainloop, args=(pipe_out,))
    light_controller.start()

    state = {
        'pattern': 'rainbow_cycle'
    }
    sleep(5)
    pipe_in.send(state)
    sleep(5)
    state = {
        'pattern': 'rainbow'
    }
    pipe_in.send(state)
    sleep(10)

def create_light_controller_process():
    queue = multiprocessing.Queue()
    light_controller = multiprocessing.Process(target=light_process_mainloop, args=(queue,))
    light_controller.start()
    return queue

def light_process_mainloop(queue):
    from .simulator import Strip  # We have to import this after the process is created
                                 # to avoid issues when forking the interpreter.
    state = {
        'pattern': 'rainbow',
        'clock_tick_size': 0.01
    }
    strip = Strip(300)


    # Set some defaults
    clock_tick_size = 0.01
    time = 0
    active_pattern = pattern_library['rainbow']



    # Mainloop
    while True:
        for index in range(300):
            strip.setPixelColor(index, active_pattern.get_color(index, time))
        strip.show()
        sleep(active_pattern.get_wait_time(time))

        """ empty the queue. if we got anything, update the state """
        received_data = check_queue(queue)
        if received_data is not None:
            for key in received_data:  
                state[key] = received_data[key]

        pattern_id = state['pattern']
        active_pattern = pattern_library[pattern_id]

        time += state['clock_tick_size']
        time = time % 1

def check_queue(queue):
    received_data = None
    while not queue.empty():
        try:
            received_data = queue.get_nowait()
        except queue.Empty:
            received_data = None

    return received_data

 