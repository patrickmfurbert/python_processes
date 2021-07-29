# Author: Patrick Furbert
# Date: 7/28/2021

import re
import sys
import os
import binascii

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


maps_file = open(f"/proc/{sys.argv[1]}/maps", 'r')
mem_file = open(f"/proc/{sys.argv[1]}/mem", 'rb', 0)
output_file = open(f"{sys.argv[1]}.dump", 'wb')

start = 0x55d6c842a000
end = 0x55d6c843a000


print()
print('----------------')
print()

mem_file.seek(start)
memory = mem_file.read(end - start)

hex = binascii.hexlify(memory).decode('ascii')

bytes = [hex[i:i+2] for i in range(0, len(hex), 2)]

for x in range(len(bytes)):
    if x % 12 != 0:
        print(bytes[x], end= ' ')
    else:
        print(bytes[x])

# output_file.write(memory)
# hex = memory.split('\x')

# for x in range(len(hex)):
#     if x % 10 == 0:
#         print(hex[x])
#     else:
#         print(hex[x], end=' ')
# for line in maps_file.readlines():  # for each mapped region
#     m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
#     if m.group(3) == 'r':  # if this is a readable region
#         start = int(m.group(1), 16)
#         end = int(m.group(2), 16)
#         mem_file.seek(start)  # seek to region start
#         chunk = mem_file.read(end - start)  # read region contents
#         output_file.write(chunk)  # dump contents to standard output
maps_file.close()
mem_file.close()
output_file.close()