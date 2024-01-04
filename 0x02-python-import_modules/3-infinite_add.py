#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) == 0:
        print(0)
    else:
        total = sum(map(int, args))
        print(total)

