import curses
import random

sentence_categories = {
    "HIGH_FREQUENCY": [
        "The quick brown fox jumps over the lazy dog",
        "She said that it was time to go home now",
        "They went to the park to play with a ball",
        "You should try to eat some good food today",
    ],
    "HOME_ROW_BASIC_FINGER_MOVEMENT": [
        "Ask the lad to add a sash to the dress",
        "All fall as the tall glass falls to the floor",
        "Dad said to add salt to the fat fish",
        "She sells shells by the side of the sea",
    ],
    "RHYTHMIC_SENTENCES": [
        "Work hard and play soft for a long life",
        "Keep your eyes on the road and your hands on the wheel",
        "Every small step leads to a very large leap",
        "Light the fire and stay warm in the cold night",
    ],
}

category_names = list(sentence_categories.keys())

def choose_sentence(stdscr):
    current_row_idx = 0
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(category_names):
            x = w//2 - len(row)//2
            y = h//2 - len(category_names)//2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    while True:
        print_menu(stdscr, current_row_idx)
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(category_names) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            chosen_category_name = category_names[current_row_idx]
            sentence_list = sentence_categories[chosen_category_name]
            return random.choice(sentence_list)
        
        print_menu(stdscr, current_row_idx)
