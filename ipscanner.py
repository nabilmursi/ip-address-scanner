import subprocess
import sys

def ping_ip(ip_address):
    try:
        # Ping the IP address once with a timeout of 1 second
        response = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return response.returncode == 0
    except subprocess.CalledProcessError:
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 ipscanner.py <start_ip> <end_ip>")
        return
    
    start_ip = sys.argv[1]
    end_ip = sys.argv[2]

    # Split the IPs into their respective components
    start_parts = list(map(int, start_ip.split('.')))
    end_parts = list(map(int, end_ip.split('.')))

    # Generate IP range
    for i in range(start_parts[2], end_parts[2] + 1):
        for j in range(start_parts[3], end_parts[3] + 1):
            ip = f"{start_parts[0]}.{start_parts[1]}.{i}.{j}"
            if ping_ip(ip):
                print(f"{ip} is online")

if __name__ == "__main__":
    main()
