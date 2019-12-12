#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 1:
        print("{:d} argument:".format(i))
        print("{:d}: {}".format(1, sys.argv[1]))
    if i == 0:
        print("{:d} arguments.".format(i))
    if i > 1:
        print("{:d} arguments:".format(i))
        for j in range(1, len(sys.argv)):
            print("{:d}: {}".format(j, sys.argv[j]))
