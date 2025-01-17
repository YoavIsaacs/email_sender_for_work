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
    stdscr.addstr(0, 0, f"You have picked: {location}. Press any key to start adding stations:")
    stdscr.getch()
    stdscr.erase()
    stdscr.refresh()

    finished_adding = False
    num_of_stations = 0
    stations = {}

    while not finished_adding:
        stdscr.addstr(0, 0, f"Adding station #{num_of_stations + 1}:")
        stdscr.addstr(1, 0, "Please enter the name of the station:")

        text = []
        cursor_pos = 0

        while True:
            stdscr.addstr(3, 0, "".join(text) + " ")
            stdscr.move(3, cursor_pos)
            curses.curs_set(1)
            stdscr.refresh()

            key = stdscr.getch()

            if key in (curses.KEY_ENTER, ord("\n"), ord ("\r")):
                break
            elif key in (curses.KEY_BACKSPACE, 137):
                if cursor_pos > 0:
                    cursor_pos -= 1
                    del text[cursor_pos]
            elif key == curses.KEY_LEFT:
                if cursor_pos > 0:
                    cursor_pos -= 1
            elif key == curses.KEY_RIGHT:
                if cursor_pos < len(text):
                    cursor_pos += 1
            elif 32 <= key <= 126:
                text.insert(cursor_pos, chr(key))
                cursor_pos += 1

        
        stations[num_of_stations] = "".join(text)
        num_of_stations += 1

        stdscr.erase()
        stdscr.refresh()
        stdscr.addstr(0, 0, f"You have added station: {stations[num_of_stations - 1]}. To add another station, press enter, to finish press any other key.")
        stdscr.refresh()

        key = stdscr.getch()

        if key not in (curses.KEY_ENTER, ord("\n"), ord ("\r")):
            finished_adding = True
        stdscr.erase()
        stdscr.refresh()




    stdscr.getch()

wrapper(main)
