import subprocess
import platform

def ping_host(host, count):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]

    try:
        response = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(response)
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {host}:")
        print(e.output)

def main():
    host = input("Enter a host to ping (e.g., google.com or 192.168.1.1): ")
    count = input("Enter the number of ping attempts: ")

    ping_host(host, count)

if __name__ == "__main__":
    main()
