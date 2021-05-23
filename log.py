from tabulate import tabulate
from datetime import date as d
FILE_NAME = "log.txt"


def check_in_file(lines, date):
    for line in lines:
        if line[0] == date:
            return True
    return False


def generate_line(date, sessions=1):
    return f"{date},{sessions}\n"


def log():
    """
    this function should log the total sessions done in a day
    if date already exists in the log.txt it shouldnt create a new one

    """
    date = str(d.today())
    with open(FILE_NAME, "r+") as file:
        lines = [x.strip("\n").split(",") for x in file.readlines()]

        if check_in_file(lines, date):
            for line in lines:
                if line[0] == date:
                    line[1] = str(int(line[1]) + 1)
                    with open(FILE_NAME, "w") as f:
                        for line in lines:
                            f.write(generate_line(date, line[1]))
        else:
            line = generate_line(date)
            file.write(line)


def create_log():
    # creating file
    try:
        f = open(FILE_NAME, "x")
    except FileExistsError:
        pass


def get_stats():
    with open(FILE_NAME, "r") as file:
        data = [x.strip("\n").split(",") for x in file.readlines()]
        table = tabulate(data, headers=["Date", "Sessions"])
        print(table)
