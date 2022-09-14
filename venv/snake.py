import math
import os
import time


class Game():
    def __init__(self):
        isActive = True
        self.sw, self.sh = os.get_terminal_size()
        while isActive:
            self.update()

    # create a little function to clear the screen
    def clear(self):
        os.system('clear')

    def draw(self):
        char = "#"
        x = 0
        y = 0
        for x in range(self.sw):
            print(char * self.sh)

    def update(self):  # screen update function
        self.clear()
        self.draw()
