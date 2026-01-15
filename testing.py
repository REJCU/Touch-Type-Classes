import curses

def main(stdscr):
    # 1. Setup Colors
    curses.start_color()
    # init_pair(pair_number, foreground, background)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE) # Inverted

    curses.curs_set(0)
    stdscr.keypad(True)
    
    y, x = 5, 5
    
    while True:
        stdscr.erase()
        
        # 2. Determine which color pair to use
        if x < 20:
            current_color = curses.color_pair(1)
        else:
            current_color = curses.color_pair(2) | curses.A_BOLD

        # 3. Render with the chosen color
        stdscr.addstr(y, x, " ● ", current_color)
        
        stdscr.addstr(0, 0, "Move right to turn RED. Press 'q' to quit.", curses.color_pair(3))
        
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:    y -= 1
        elif key == curses.KEY_DOWN:  y += 1
        elif key == curses.KEY_LEFT:  x -= 1
        elif key == curses.KEY_RIGHT: x += 1

curses.wrapper(main)
