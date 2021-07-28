# Author: Patrick Furbert
# Date: 7/28/2021

import re
import sys
import os

maps = []
shared_objects = set()

expression = '([0-9A-Fa-f]+-[0-9A-Fa-f]+) ([-r][-w][-x][-p])'

regex = re.compile(expression)

with open(f'/proc/{sys.argv[1]}/maps') as file:
    maps = [line.rstrip() for line in file]


print(f'Address Ranges Executable Pages in Proccess <{sys.argv[1]}>:')
for line in maps:
    try:
        if 'x' in regex.search(line).group(2):
            print(regex.search(line).group(1))
    except AttributeError:
        pass


