# Author: Patrick Furbert
# Date: 7/26/2021
# This program spawns four threads that go to sleep for 25 seconds

import time
import concurrent.futures

def function_sleep():
    time.sleep(25)

def main():
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for x in range(4):
            executor.submit(function_sleep)

if __name__ == "__main__":
    main()