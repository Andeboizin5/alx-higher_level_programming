#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 arguments.")
else:
    plural = "s" if num_args > 1 else ""
    print(f"{num_args} argument{plural}:")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")

