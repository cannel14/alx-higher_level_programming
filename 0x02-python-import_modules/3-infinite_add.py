#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for j in argv[1:]:
        add += int(j)
        print("{:d}".format(add))
