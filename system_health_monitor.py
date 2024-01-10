import psutil
import socket

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_memory_usage():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.used / (1024**2):.2f} MB / {memory.total / (1024**2):.2f} MB"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB"

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"Hostname: {hostname}, IP Address: {ip_address}"

def display_system_health():
    print(get_cpu_usage())
    print(get_memory_usage())
    print(get_disk_usage())
    print(get_network_info())

def main():
    display_system_health()

if __name__ == "__main__":
    main()
