import curses
from curses import wrapper

from utils import EMAILS

def main(stdscr) -> None:
    stdscr.clear()
    num = 1
    stdscr.addstr(0, 0, "EMAILS", curses.A_REVERSE)
    for key in EMAILS:
        stdscr.addstr(num, 0,"[ ]" + key + ": ")
        num += 1
    
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
