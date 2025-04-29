#Lab Assignment - CPU Usage
#By: Brian Duke
#Date: 4/25/2025
#This program - simple CPU usage monitoring tool using Python. It will display the CPU usage statistics of the system using psutil.

import psutil
import logging
import time

logging.basicConfig(filename='system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1) 
    logging.info(f"CPU Usage: {cpu_percent}%") 
def main():
    print("Starting CPU Usage Monitoring...")
    for _ in range(5): 
        log_cpu_usage()
        time.sleep(2) 
    print("CPU usage monitoring finished. Check system.log for results.")

if __name__ == "__main__":
    main()