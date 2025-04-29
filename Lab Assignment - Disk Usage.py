#Lab Assignment - Disk Usage
#By: Brian Duke
#Date: 4/25/2025
#This program - simple disk usage monitoring tool using Python. It will display the disk usage statistics of the system using shutil.

import shutil
import os

def get_disk_usage(path):
    try:
        total, used, free = shutil.disk_usage(path)
        return total, used, free
    except FileNotFoundError:
        print(f"Error: Path '{path}' not found.")
        return None
    
def format_size(size_bytes):
    gb = size_bytes / (1024 ** 3)
    return f"{gb:.2f} GB"

def display_disk_usage(path):
    print(f"Disk Usage for: {path}")
    usage = get_disk_usage(path)
    if usage:
        total, used, free = usage
        print(f"Total Space: {format_size(total)}")
        print(f"Used Space: {format_size(used)}")
        print(f"Free Space: {format_size(free)}")

def main():
    paths_to_monitor = ['/', 'C:\\']
    print("Starting Disk Usage Monitor...")
    for path in paths_to_monitor:
        display_disk_usage(path)
        print("-" * 20)
    print("Disk Usage Monitoring Finished.")

if __name__ == "__main__":
    main()