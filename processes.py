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
        print(str(output, encoding)) #output is a byte, but we need it as astring(hence we must decode the byte string and make it a character(unicode) string)

    def print_help(self):
        """
        Print help menu
        """

        help = 'Process Tool Help\n' \
             '1.) No arguments - Prints the help\n' \
             '2.) rp - Prints running process\n' \
             '3.) rt - Prints running threads within process boundary\n' \
             '4.) lm - Prints loaded modules within the processes\n '
        
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
            pass

    else:
        processes.print_help()    


if __name__ == "__main__":
    main()
