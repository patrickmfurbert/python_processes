# Author: Patrick Furbert
# Date: 7/26/2021

import binascii
import subprocess
import sys
import re

class process_tool:


    def print_processes(self):
        """
        Prints out the
        current running processes
        """
        encoding = 'utf-8' 
        command = 'ps -ac -o user,pid,cmd' #running processes, cmd name based on exe, and pid
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        
        #output is a byte, but we need it as a string- hence we must decode the byte string and make it a character(unicode) string
        print(str(output, encoding)) 

    def print_threads(self, pid):
        """
        Lists all of the running threads
        within the process boundary
        """
        encoding = 'utf-8'
        command = f'ps -T -p {pid} -o user,pid,spid,cmd'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        #output is a byte, but we need it as a string- hence we must decode the byte string and make it a character(unicode) string
        print(str(output, encoding))

    def print_loaded_modules(self, pid):
        """
        Prints shared objects for the 
        specified pid
        """
        maps = []
        shared_objects = set()

        with open(f'/proc/{pid}/maps') as file:
            maps = [line.rstrip() for line in file]

        for line in maps:
            if '.so' in line.split('/')[-1]:
                shared_objects.add(line.split('/')[-1])

        for object in shared_objects:
            print(object)

    def print_executable_pages(self, pid):
        """
        Prints the address ranges for the executable
        pages in the process
        """
        # Regular Expression
        expression = '([0-9A-Fa-f]+-[0-9A-Fa-f]+) ([-r][-w][-x][-p])'

        # Regular Expresson Object
        regex = re.compile(expression)

        # open maps 
        with open(f'/proc/{pid}/maps') as file:
            maps = [line.rstrip() for line in file]

        # get the address ranges of the executatble pages
        print(f'Address Ranges Executable Pages in Proccess {pid}:')
        for line in maps:
            try:
                if 'x' in regex.search(line).group(2):
                    print(regex.search(line).group(1))
            except AttributeError:
                pass
        
    def print_memory(self, pid, start, end):
        """
        prints memory for 
        specified start and end address
        """
        start_addr = int('0x' + start, 16)
        end_addr = int('0x' + end, 16)
        mem_file = open(f"/proc/{pid}/mem", 'rb', 0)
        mem_file.seek(int(start_addr))
        hex = binascii.hexlify(mem_file.read(end_addr-start_addr)).decode('ascii')

        bytes = [hex[i:i+2] for i in range(0, len(hex), 2)]

        for x in range(len(bytes)):
            if x % 12 != 0:
                print(bytes[x], end= ' ')
            else:
                print(bytes[x])

    def print_help(self):
        """
        Print help menu
        """

        help = 'Process Tool Help\n' \
             '1.) No arguments - Prints the help\n' \
             '2.) rp           - Prints running process\n' \
             '3.) rt <pid>     - Prints running threads in multithread process\n' \
             '4.) lm <pid>     - Prints loaded modules within the processes\n' \
             '5.) ep <pid>     - Prints address ranges for executable pages within process\n' \
             '6.) rm <pid> <start_address> <end_address> - Dumps memory for specified addresses\n'
        
        print(help)


def main():

    # create process_tool object
    processes = process_tool()

    # check for two arguments
    if len(sys.argv) > 1:

        # print running process
        if sys.argv[1] == "rp":
            processes.print_processes()
        
        # print running threads within process boundary
        if sys.argv[1] == "rt":
            # first check if there is a second argument
            if len(sys.argv) >= 3:
                #check if the third argument is a number
                try:
                    val = int(sys.argv[2])
                except ValueError:
                    print('Enter valid process id(Integer')
                
                #run command to print process id
                processes.print_threads(val)

        # print loaded modules for specified process
        if sys.argv[1] == "lm":
            # first check if there is a second argument
            if len(sys.argv) >= 3:
                #check if the third argument is a number
                try:
                    val = int(sys.argv[2])
                except ValueError:
                    print('Enter valid process id(Integer')
                
                #run command to print process id
                processes.print_loaded_modules(val)

        # print loaded modules for specified process
        if sys.argv[1] == "ep":
            # first check if there is a second argument
            if len(sys.argv) >= 3:
                #check if the third argument is a number
                try:
                    val = int(sys.argv[2])
                except ValueError:
                    print('Enter valid process id(Integer')
                
                #run command to print process id
                processes.print_executable_pages(val)
        
        # print memory for specified process at starting and ending address
        if sys.argv[1] == "rm":
            # first check if there is a second argument
            if len(sys.argv) == 5:
                #check if the third argument is a number
                try:
                    val = int(sys.argv[2])
                except ValueError:
                    print('Enter valid process id(Integer')
                
                #run command to print process id
                processes.print_memory(val, sys.argv[3], sys.argv[4])
        

        
    else:
        processes.print_help()    


if __name__ == "__main__":
    main()
