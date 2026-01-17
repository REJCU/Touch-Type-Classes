from sentence_choice import choose_sentence
from engine import TypeEngine
from ui import TypingUI
import curses

def main(stdscr):
    sentence = choose_sentence(stdscr)
    ui = TypingUI(stdscr)
    engine = TypeEngine(sentence)

    while True:
        ui.render(engine.target, engine.current_input)

        if len(engine.current_input) >= len(engine.target):
            break 

        key = ui.get_input()

        if key:
            engine.process_key(key)

if __name__ == "__main__":
    curses.wrapper(main)
