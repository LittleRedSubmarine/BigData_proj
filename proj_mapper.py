#! /usr/bin/env python3

import sys

for line in sys.stdin:
    input_data = line.strip().split('; ')
    p_name = input_data[0]
    p_goal = input_data[1]
    p_assist = input_data[2]

    print(f"{p_name}\t{p_goal}\t{p_assist}")
