import colorsys

class Color:
    def __init__(self, red, green, blue, white=0, hsv=False):
        self.red = self.clamp(red)
        self.green = self.clamp(green)
        self.blue = self.clamp(blue)
        self.white = self.clamp(white)
        
    def clamp(self, number):
        return min(max(round(number), 0), 255)

    def setBrightness(self, brightness):
        self.red = round(brightness * self.red)
        self.green = round(brightness * self.green)
        self.blue = round(brightness * self.blue)
        self.white = round(brightness * self.white)

    def voltageOffset(self, index):
        position = index/299.0
        self.red =  (1 - 0.5*position) * self.red


class Pattern:
    def __init__(self):
        self.name = "default"

    def __str__(self):
        return self.display_name

    # (index, time) --> (red, green, blue, white)
    # Or really, a map  f : N x S^1 --> R^4
    def get_color(self, index, time, **kwargs):
        return (0, 0, 0, 0)


    def get_wait_time(self, time, **kwargs):
        return 10


# Auxillary Functions
def clamp(number):
    return min(max(round(number), 0), 255)

#------        ------#
#      Patterns      #
#--------------------#


class Rainbow(Pattern):
    def __init__(self):
        self.id_name = "rainbow"
        self.display_name = "Rainbow"
        self.test = 2

    def get_color(self, index, time, **kwargs):
        red, green, blue = colorsys.hsv_to_rgb(time, 1, 1)
        return Color(255*red, 255*green, 255*blue)

class GentleWhite(Pattern):
    def __init__(self):
        self.id_name = "gentle_white"
        self.display_name = "Gentle White"

    def get_color(self, index, time, **kwargs):
        return Color(0, 0, 0, 200)

class RainbowCycle(Pattern):
    def __init__(self):
        self.id_name = "rainbow_cycle"
        self.display_name = "Rainbow Cycle"

    def get_color(self, index, time, **kwargs):
        normalized_sum = (index/300.0 + time) % 1
        red, green, blue = colorsys.hsv_to_rgb(normalized_sum, 1, 1)
        return Color(255*red, 255*green, 255*blue)

class AdjustedRainbowCycle(Pattern):
    def __init__(self):
        self.id_name = "adjusted_rainbow_cycle"
        self.display_name = "Adjusted Rainbow Cycle"

    def get_color(self, index, time, **kwargs):
        normalized_sum = (index/300.0 + time- 0.1) % 1
        normalized_sum = (normalized_sum)**1.5
        red, green, blue = colorsys.hsv_to_rgb(normalized_sum, 1, 1)
        return Color(255*red, 255*green, 255*blue)

class AdjustedRainbow(Pattern):
    def __init__(self):
        self.id_name = "adjusted_rainbow"
        self.display_name = "Adjusted Rainbow"

    def get_color(self, index, time, **kwargs):
        normalized_sum = (time- 0.1) % 1
        normalized_sum = (normalized_sum)**1.5
        red, green, blue = colorsys.hsv_to_rgb(normalized_sum, 1, 1)
        return Color(255*red, 255*green, 255*blue)

class RedTest(Pattern):
    def __init__(self):
        self.id_name = "red_test"
        self.display_name = "Red Test"

    def get_color(self, index, time, **kwargs):
        normalized_sum = 0
        if 0 <= index < 60:
            normalized_sum = 0
        elif 60 < index < 120:
            normalized_sum = 0.01
        elif 180 < index < 240:
            normalized_sum = 0.02
        elif 240 < index <= 300:
            normalized_sum = 1 - 0.01
        # normalized_sum = (normalized_sum)**1.5
        red, green, blue = colorsys.hsv_to_rgb(normalized_sum, 1, 1)
        return Color(255*red, 255*green, 255*blue)



pattern_library = {
    "rainbow": Rainbow(),
    "rainbow_cycle": RainbowCycle(),
    "adjusted_rainbow_cycle": AdjustedRainbowCycle(),
    "adjusted_rainbow": AdjustedRainbow(),
    "red_test": RedTest(),
    "gentle_white": GentleWhite()
}
