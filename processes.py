# Author: Patrick Furbert
# Date: 7/26/2021

import subprocess
import sys

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



    def print_help(self):
        """
        Print help menu
        """

        help = 'Process Tool Help\n' \
             '1.) No arguments - Prints the help\n' \
             '2.) rp           - Prints running process\n' \
             '3.) rt <pid>     - Prints running threads within process boundary\n' \
             '4.) lm <pid>     - Prints loaded modules within the processes\n '
        
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
        

    else:
        processes.print_help()    


if __name__ == "__main__":
    main()
