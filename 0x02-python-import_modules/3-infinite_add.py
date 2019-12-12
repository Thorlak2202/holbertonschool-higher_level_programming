#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("{:d}".format(i))
    if i >= 1:
        h = 0
        for j in range(1, len(sys.argv)):
            h += int(sys.argv[j])
        print("{:d}".format(h))
