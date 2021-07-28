# Author: Patrick Furbert
# Date: July 27, 2021

import os
import sys

maps = []
shared_objects = set()


with open(f'/proc/{sys.argv[1]}/maps') as file:
    maps = [line.rstrip() for line in file]

for line in maps:
    if '.so' in line.split('/')[-1]:
        shared_objects.add(line.split('/')[-1])


# for object in shared_objects:
#     print(object)

for object in maps:
    print(maps)



# directory_tree = []

# for root, dir, files in os.walk('/proc'):
#     directory_tree.append((root, dir, files))


# for entry in directory_tree:
#     print(entry)