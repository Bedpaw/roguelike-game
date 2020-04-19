# utils for reading/writing to files


def return_each_row(filename, *args):
    with open("filename", "r") as f:
        for row in f:
            return row
