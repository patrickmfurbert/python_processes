# Author: Patrick Furbert
# Date: 7/26/2021

import subprocess

class process_tool:


    def print_processes(self):
        """
        Prints out the
        current running processes
        """
        command = 'ps'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print(output)



def main():
    processes = process_tool()

    # print running processes
    processes.print_processes()


if __name__ == "__main__":
    main()
