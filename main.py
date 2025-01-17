import curses
from curses import wrapper

from utils import EMAILS, LOCATIONS

def main(stdscr) -> None:
    stdscr.clear()
    num = 2
    location = ""
    location_picked = False

    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.attron(curses.A_BOLD)

    stdscr.addstr(0, 0, "Please select the location you worked at using enter or space:")

    for loc in LOCATIONS:
        stdscr.addstr(num, 0, "[ ] " + loc)
        num +=1

    x, y = 0, 0
    
    stdscr.refresh()
    while not location_picked:

        char_under_cursor = stdscr.inch(y, x) & 0xFF
        if char_under_cursor != ord(" "):
            stdscr.addch(y, x, char_under_cursor, curses.A_REVERSE)
        else:
            stdscr.addch(y, x, ' ', curses.A_REVERSE)

        stdscr.refresh()


        key = stdscr.getch()

        stdscr.addch(y, x, char_under_cursor if char_under_cursor != ord(" ") else " ")
        
        if key == curses.KEY_UP and y > 0:
            y -= 1
        elif key == curses.KEY_DOWN and y < curses.LINES:
            y += 1
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < curses.COLS:
            x += 1

        stdscr.refresh()

        if key == curses.KEY_ENTER or key == ord(" ") or key == ord("\r") or key == ord("\n"):
            if 2 <= y <= len(LOCATIONS) + 1:
                stdscr.addch(y, 1, "O")
                location_picked = True
                location = LOCATIONS[y - len(LOCATIONS) - 2]

    stdscr.erase()
    stdscr.addstr(0, 0, f"You have picked: {location}")
    stdscr.refresh()



    stdscr.getch()

wrapper(main)
