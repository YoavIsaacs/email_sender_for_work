import curses
from curses import wrapper

from utils import EMAILS, LOCATIONS

def main(stdscr) -> None:
    stdscr.clear()
    num = 1
    location = ""

    for loc in LOCATIONS:
        stdscr.addstr(num, 0, "[ ] " + loc)
        num +=1


    stdscr.refresh()
    stdscr.getch()

wrapper(main)
