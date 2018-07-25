import multiprocessing
from patterns import pattern_library
from time import sleep

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

def light_process_mainloop(pipe_out):
    from simulator import Strip  # We have to import this after the process is created
                                 # to avoid issues when forking the interpreter.


    state = {
        'pattern': 'rainbow',
        'clock_tick_size': 0.01
    }

    strip = Strip(300)
    clock_tick_size = 0.01
    time = 0
    activePattern = pattern_library['rainbow']
    while True:
        for index in range(300):
            strip.setPixelColor(index, activePattern.get_color(index, time))
        strip.show()
        sleep(activePattern.get_wait_time(time))

        if pipe_out.poll():
            receivedData = pipe_out.rcev() # This syntax is made up
            for key in receivedData:
                state[key] = receivedData[key]

        activePattern = pattern_library[state['pattern']]

        time += clock_tick_size
        time = time % 1




    