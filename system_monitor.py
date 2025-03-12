import psutil  # This helps us get CPU and memory info
import time    # This helps us wait a few seconds

while True:  # This makes the program run forever
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage
    memory_usage = psutil.virtual_memory().percent  # Get memory usage

    print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")  # Show result

    time.sleep(5)  # Wait for 5 seconds before checking again
