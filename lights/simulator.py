from tkinter import Tk, Label, Button, Canvas



WINDOW_SIZE = 1200


# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)


class Strip:
    def __init__(self, led_count):

        self.led_count = led_count
        self.master = master = Tk()
        master.title("Simulating LED strip")

        self.window_size = WINDOW_SIZE

        self.canvas = Canvas(master, width=self.window_size, height=20, bd=0, highlightthickness=0)
        self.canvas .pack()

        self.pixels = []
        for i in range(led_count):
            pixel_width = self.window_size/led_count
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

    def begin(self):    # This is just to match the syntax of the neopixel library
        pass            # we don't need it to do anything.






