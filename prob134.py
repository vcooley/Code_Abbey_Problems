"""
Flying Text ScreenSaver.
Track the position of a screensaver given the width and height of the screen
and the length of the string of text to fly around.
"""

__author__ = 'Vince'

class ScreenSaverTracker(object):
    """
    Tracks the position of the beginning of the text of a flying text screen saver
    """
    def __init__(self,  screen_width, screen_height, string_length):
        self.width = screen_width
        self.height = screen_height
        self.length = string_length
        self.last_char_at = self.end_position()
        self.current_position = (0, 0)
        self.step = (1, 1)

    def end_position(self):
        """
        Gives the x position of the last value in the string
        :return:
        """
        while True:
            yield self.current_position[0] + self.length - 1

    def stepper(self):
        """
        Moves the text to the next step, first modifying the step if the result
        would put the text off screen.
        :return new_position:
        """
        if self.last_char_at.next() + self.step[0] >= self.width\
           or self.current_position[0] + self.step[0] < 0:
            self.step = (-1 * self.step[0], self.step[1])
        if self.current_position[1] + self.step[1] >= self.height\
           or self.current_position[1] + self.step[1] < 0:
            self.step = (self.step[0], -1 * self.step[1])
        self.current_position = (self.current_position[0] + self.step[0],
                                 self.current_position[1] + self.step[1])

    def tracker(self, number_steps):
        """
        Prints the position of the first letter in the screen after each step
        for number_steps times.
        :return:
        """
        for i in range(number_steps):
            print self.current_position[0], self.current_position[1],
            self.stepper()


def main():
    with open('test.txt') as data_file:
        width, height, length = map(int, data_file.readline().split())
        screensaver = ScreenSaverTracker(width, height, length)
        screensaver.tracker(101)

if __name__ == "__main__":
    main()