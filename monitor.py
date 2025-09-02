import psutil

"""
Script to monitor CPU health in windows local machine and ubuntu Servers
"""

# CPU Threshold
CPU_THRESHOLD = 80
INTERVAL = 2 # Sets the time interval on which the psutil has to check the cpu_percent

while True:
    try:
        cpu_usage = psutil.cpu_percent(INTERVAL) # interval in seconds
        if cpu_usage <= CPU_THRESHOLD:
            print(f"🖥️ Monitoring CPU usage......Current utilisation: {cpu_usage}%")
        else:
            memory_info = psutil.virtual_memory()
            print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}% | Memory Usage: {memory_info.percent}% ")
           

    except Exception as e:
        print(f"Error occurred: {e}")
        break  # Exit the loop if an error occurs