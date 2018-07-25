import colorsys

class Color:
    def __init__(self, red, green, blue, white=0, hsv=False):
        self.red = self.clamp(red)
        self.green = self.clamp(green)
        self.blue = self.clamp(blue)
        self.white = self.clamp(white)
        
    def clamp(self, number):
        return min(max(round(number), 0), 255)




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
        return 0.1


# Auxillary Functions
def clamp(number):
    return min(max(round(number), 0), 255)

#------        ------#
#      Patterns      #
#--------------------#


class Rainbow(Pattern):
    def __init__(self):
        self.api_name = "rainbow"
        self.display_name = "Rainbow"
        self.test = 2

    def get_color(self, index, time, **kwargs):
        red, green, blue = colorsys.hsv_to_rgb(time, 1, 1)
        return Color(255*red, 255*green, 255*blue)



class RainbowCycle(Pattern):
    def __init__(self):
        self.api_name = "rainbow_cycle"
        self.display_name = "Rainbow Cycle"

    def get_color(self, index, time, **kwargs):
        normalized_sum = (index/300.0 + time) % 1
        red, green, blue = colorsys.hsv_to_rgb(normalized_sum, 1, 1)
        return Color(255*red, 255*green, 255*blue)



pattern_library = {
    "rainbow": Rainbow(),
    "rainbow_cycle": RainbowCycle()
}
