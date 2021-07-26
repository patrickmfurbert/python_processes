# Author: Patrick Furbert
# Date: 7/26/2021

import time
import concurrent.futures

def function_sleep():
    time.sleep(20)

def main():
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #     executor.map(function_sleep)
    function_sleep()

if __name__ == "__main__":
    main()