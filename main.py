import time as t
from log import get_stats, create_log
from timer import timer


def main():
    create_log()
    while (inp := input(">> ")) and inp != "exit":
        if inp == "start":
            timer()
        elif inp == "stat":
            get_stats()


main()
