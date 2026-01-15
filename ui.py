# https://docs.python.org/3/howto/curses.html
import curses

class TypingUI:
    def __init__(self, stdsrc):
    self.stdscr = stdscr
    self.setup_colors()


    def setup_color(self):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)


    def render():


    def get_input():
        key = stdsrc.getch()

        if key == "Backspace":
            curses.color_pair(2)


