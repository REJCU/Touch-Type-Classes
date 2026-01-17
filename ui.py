# https://docs.python.org/3/howto/curses.html
import curses

class TypingUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.setup_color()

    def setup_color(self):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def render(self, target, current_input):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        
        # Display the target sentence
        self.stdscr.addstr(height // 2 - 1, 0, target)
        
        # Display the user's input
        for i, char in enumerate(current_input):
            correct_char = target[i]
            if char == correct_char:
                self.stdscr.addstr(height // 2, i, char, curses.color_pair(1))
            else:
                self.stdscr.addstr(height // 2, i, char, curses.color_pair(2))

        self.stdscr.refresh()

    def get_input(self):
        key = self.stdscr.getch()

        if key in (curses.KEY_BACKSPACE, 127, 8):
            return "BACKSPACE"
        
        if key >= 32 and key <= 126:
            return chr(key)
        
        return None
