# python_processes

Uses Python 3.9.2 64-bit on Kali Linux

type python3 processes.py for help menu

Example commands: 

python3 processes.py rp (Prints running process)
python3 processes.py rt <pid> (Prints threads for a specified multithread process)
python3 processes.py lm <pid> (Prints shared objects for specified process)
python3 processes.py ep <pid> (Prints address ranges for executable pages)
python3 processes.py rm <pid> <start_address> <end_address> (prints memory for specified addresses range)