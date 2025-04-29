#Lab Assignment - System Monitoring
#By: Brian Duke
#Date: 4/25/2025
#This program - simple system monitoring tool using Python. It will display the CPU, memory, and disk usage statistics of the system at regular intervals. 

import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def display_system_info():
    count = 0
    print("Monitoring System Statistics...")
    while count < 5:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage (root): {disk_usage}%")
        print("-" * 20)
        time.sleep(5)  
        count += 1 
    print("Monitoring Finished.")

def main():
    print("Starting System Monitor...")
    display_system_info()

if __name__ == "__main__":
    main()