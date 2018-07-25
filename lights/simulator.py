from tkinter import Tk, Label, Button, Canvas
from time import sleep

from patterns import pattern_library

# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)




class Strip:
    def __init__(self, led_count):

        self.led_count = led_count
        self.master = master = Tk()
        master.title("Simulating LED strip")

        self.width = 3600

        self.canvas = Canvas(master, width=self.width, height=20, bd=0, highlightthickness=0)
        self.canvas .pack()

        self.pixels = []
        for i in range(led_count):
            pixel_width = self.width/led_count
            left_endpoint = pixel_width*i
            right_endpoint = pixel_width*(i+1)
            pixel = self.canvas.create_rectangle(left_endpoint, 0, right_endpoint, 20, fill="white", outline="white")
            self.pixels.append(pixel)

    def setPixelColor(self, index, color):
        pixel = self.pixels[index]
        color_as_hex = '#%02x%02x%02x' % (color.red, color.green, color.blue)
        self.canvas.itemconfig(pixel, fill=color_as_hex, outline=color_as_hex)

    def show(self):
        self.master.update()

    def numPixels(self):
        return self.led_count

    def begin(self):
        pass




def mainloop():
    strip = Strip(300)
    clock_tick_size = 0.01
    time = 0
    activePattern = pattern_library['rainbow']
    while True:
        for index in range(300):
            strip.setPixelColor(index, activePattern.get_color(index, time))
        strip.show()
        sleep(activePattern.get_wait_time(time))
        time += clock_tick_size
        time = time % 1

mainloop()